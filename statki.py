import pygame
import sys
import graphics as gfx
from objects import Ship, Treasure
from economy import Economy
from game_logic import GameLogic

class BattleshipGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((gfx.WIDTH, gfx.HEIGHT))
        pygame.display.set_caption("Projekt Statki - Zespół NPG")
        self.clock = pygame.time.Clock()
        
        # Szuflady na dane
        self.player_ships = []
        self.computer_ships = []
        self.player_misses = set()
        self.computer_misses = set()
        
        # Moduły zespołu
        self.eco = Economy() 
        self.treasure = Treasure(gfx.GRID_SIZE)
        
        # Zarządzanie stanem gry
        self.bomb_mode = False 
        self.game_phase = 'SETUP' 
        self.current_ship_index = 0
        self.orientation = 'H' 
        self.game_over = False
        self.winner_text = ""
        
        # Przyciski UI
        self.action_btn_rect = pygame.Rect(gfx.WIDTH//2 - 125, 660, 250, 40)
        self.bomb_toggle_btn_rect = pygame.Rect(gfx.WIDTH//2 - 125, 600, 250, 40)
        
        self.buy_ammo_btn_rect = pygame.Rect(100, 540, 380, 40)
        self.buy_repair_btn_rect = pygame.Rect(520, 540, 380, 40)
        self.buy_bomb_btn_rect = pygame.Rect(100, 590, 380, 40)
        self.buy_refinery_btn_rect = pygame.Rect(520, 590, 380, 40)
        
        # Startowe rozstawienie komputera
        GameLogic.place_random_ships(self.computer_ships, gfx.SHIP_SIZES, gfx.GRID_SIZE)

    def handle_mouse_click(self, pos):
        """Główna funkcja Franka - steruje logiką zależnie od fazy gry."""
        if self.game_over: return
        x, y = pos

        # --- FAZA 1: ROZSTAWIENIE ---
        if self.game_phase == 'SETUP':
            if self.action_btn_rect.collidepoint(pos):
                self.orientation = 'V' if self.orientation == 'H' else 'H'
                return
            if gfx.P1_OFFSET_X <= x <= gfx.P1_OFFSET_X + gfx.GRID_SIZE * gfx.CELL_SIZE and \
               gfx.P1_OFFSET_Y <= y <= gfx.P1_OFFSET_Y + gfx.GRID_SIZE * gfx.CELL_SIZE:
                c = (x - gfx.P1_OFFSET_X) // gfx.CELL_SIZE
                r = (y - gfx.P1_OFFSET_Y) // gfx.CELL_SIZE
                self.place_player_ship(r, c)

        # --- FAZA 2: STRZELANIE I BOMBARDOWANIE ---
        elif self.game_phase == 'SHOOT':
            if self.bomb_toggle_btn_rect.collidepoint(pos) and self.eco.bombardments > 0:
                self.bomb_mode = not self.bomb_mode
                return

            if gfx.P2_OFFSET_X <= x <= gfx.P2_OFFSET_X + gfx.GRID_SIZE * gfx.CELL_SIZE and \
               gfx.P2_OFFSET_Y <= y <= gfx.P2_OFFSET_Y + gfx.GRID_SIZE * gfx.CELL_SIZE:
                c = (x - gfx.P2_OFFSET_X) // gfx.CELL_SIZE
                r = (y - gfx.P2_OFFSET_Y) // gfx.CELL_SIZE
                
                # Zrzucenie bomby 2x5
                if self.bomb_mode and self.eco.bombardments > 0:
                    self.eco.bombardments -= 1
                    self.bomb_mode = False 
                    for dr in range(2):
                        for dc in range(5):
                            target_r, target_c = r + dr, c + dc
                            if 0 <= target_r < gfx.GRID_SIZE and 0 <= target_c < gfx.GRID_SIZE:
                                self.apply_player_shot(target_r, target_c)
                else:
                    # Zwykły strzał (Sprawdzenie amunicji!)
                    if self.eco.ammo <= 0: return 
                    self.eco.ammo -= 1
                    self.apply_player_shot(r, c)

                # Warunki zwycięstwa i tura komputera
                if all(ship.is_sunk() for ship in self.computer_ships):
                    self.game_over = True
                    self.winner_text = "Wygrałeś! Zniszczyłeś flotę komputera!"
                else:
                    GameLogic.computer_shoot(self.player_ships, self.player_misses, gfx.GRID_SIZE)
                    if all(ship.is_sunk() for ship in self.player_ships):
                        self.game_over = True
                        self.winner_text = "Przegrałeś! Komputer zniszczył Twoją flotę."
                    else:
                        self.game_phase = 'SHOP'

        # --- FAZA 3: SKLEP ---
        elif self.game_phase == 'SHOP':
            if self.buy_ammo_btn_rect.collidepoint(pos): self.eco.buy_item('ammo', self.player_ships)
            elif self.buy_repair_btn_rect.collidepoint(pos): self.eco.buy_item('repair', self.player_ships)
            elif self.buy_bomb_btn_rect.collidepoint(pos): self.eco.buy_item('bomb', self.player_ships)
            elif self.buy_refinery_btn_rect.collidepoint(pos): self.eco.buy_item('refinery', self.player_ships)
            elif self.action_btn_rect.collidepoint(pos): self.game_phase = 'MOVE'

        # --- FAZA 4: RUCH ---
        elif self.game_phase == 'MOVE':
            if self.action_btn_rect.collidepoint(pos):
                self.move_all_ships()
                self.game_phase = 'SHOOT' 
                
            # Obracanie własnych statków
            elif gfx.P1_OFFSET_X <= x <= gfx.P1_OFFSET_X + gfx.GRID_SIZE * gfx.CELL_SIZE and \
                 gfx.P1_OFFSET_Y <= y <= gfx.P1_OFFSET_Y + gfx.GRID_SIZE * gfx.CELL_SIZE:
                c = (x - gfx.P1_OFFSET_X) // gfx.CELL_SIZE
                r = (y - gfx.P1_OFFSET_Y) // gfx.CELL_SIZE
                for ship in self.player_ships:
                    if (r, c) in ship.cells:
                        ship.manually_rotate(gfx.GRID_SIZE, self.player_ships)
                        break

    def apply_player_shot(self, r, c):
        if (r, c) in self.computer_misses: return
        for ship in self.computer_ships:
            if (r, c) in ship.cells:
                idx = ship.cells.index((r, c))
                if not ship.health[idx]: return 
                was_sunk = ship.is_sunk()
                ship.health[idx] = False
                self.eco.credits += 50 
                if not was_sunk and ship.is_sunk():
                    self.eco.credits += 150 
                return 
        self.computer_misses.add((r, c)) 

    def place_player_ship(self, r, c):
        size = gfx.SHIP_SIZES[self.current_ship_index]
        if self.orientation == 'H':
            if c + size > gfx.GRID_SIZE: return
            cells = [(r, c + i) for i in range(size)]
            direction = (0, 1) 
        elif self.orientation == 'V':
            if r + size > gfx.GRID_SIZE: return
            cells = [(r + i, c) for i in range(size)]
            direction = (1, 0) 

        for existing_ship in self.player_ships:
            if any(cell in existing_ship.cells for cell in cells): return

        self.player_ships.append(Ship(size, cells, direction))
        self.current_ship_index += 1
        if self.current_ship_index == len(gfx.SHIP_SIZES):
            self.treasure.spawn(self.player_ships)
            self.game_phase = 'SHOOT'

    def move_all_ships(self):
        has_ref = any(s.is_refinery and not s.is_sunk() for s in self.player_ships)
        self.eco.apply_passive_income(has_ref)
            
        self.treasure.move()
        GameLogic.process_fleet_movement(self.player_ships, gfx.GRID_SIZE)
        GameLogic.process_fleet_movement(self.computer_ships, gfx.GRID_SIZE)
        
        if self.treasure.pos:
            for ship in self.player_ships:
                if not ship.is_sunk() and self.treasure.pos in ship.cells:
                    self.eco.credits += 200
                    self.treasure.spawn(self.player_ships)
                    break

    def draw(self):
        self.screen.fill(gfx.BG_COLOR)

        stats_text = gfx.title_font.render(f"KREDYTY: {self.eco.credits}  |  AMUNICJA: {self.eco.ammo}  |  BOMBY: {self.eco.bombardments}", True, gfx.YELLOW)
        self.screen.blit(stats_text, (gfx.WIDTH//2 - stats_text.get_width()//2, 10))

        p1_title = gfx.title_font.render("Twoja Plansza", True, gfx.WHITE)
        p2_title = gfx.title_font.render("Plansza Komputera", True, gfx.WHITE)
        self.screen.blit(p1_title, (gfx.P1_OFFSET_X, gfx.P1_OFFSET_Y - 40))
        self.screen.blit(p2_title, (gfx.P2_OFFSET_X, gfx.P2_OFFSET_Y - 40))

        gfx.draw_fleet_and_misses(self.screen, self.player_ships, self.player_misses, gfx.P1_OFFSET_X, gfx.P1_OFFSET_Y, self.game_over, is_player_board=True, treasure_pos=self.treasure.pos)
        gfx.draw_fleet_and_misses(self.screen, self.computer_ships, self.computer_misses, gfx.P2_OFFSET_X, gfx.P2_OFFSET_Y, self.game_over, hide_ships=not self.game_over)

        if self.game_over:
            color = gfx.GREEN if "Wygrałeś" in self.winner_text else gfx.RED
            msg = gfx.title_font.render(self.winner_text, True, color)
            self.screen.blit(msg, (gfx.WIDTH//2 - msg.get_width()//2, 60))
            
        elif self.game_phase == 'SETUP':
            size = gfx.SHIP_SIZES[self.current_ship_index]
            msg = gfx.font.render(f"Rozstaw statek: {size} masztów.", True, gfx.WHITE)
            self.screen.blit(msg, (gfx.WIDTH//2 - msg.get_width()//2, 60))
            dir_text = 'Kierunek: POZIOMO' if self.orientation == 'H' else 'Kierunek: PIONOWO'
            gfx.draw_button(self.screen, self.action_btn_rect, dir_text, gfx.YELLOW)
            
        elif self.game_phase == 'SHOOT':
            has_ref = any(s.is_refinery and not s.is_sunk() for s in self.player_ships)
            if self.bomb_mode:
                msg = gfx.font.render("TRYB BOMBARDOWANIA! Kliknij cel (obszar 2x5 w dół i prawo).", True, gfx.ORANGE)
            elif self.eco.ammo > 0:
                msg = gfx.font.render(f"Pasywny przychód: +{25 + (50 if has_ref else 0)} CR! Strzelaj!", True, gfx.RED)
            else:
                msg = gfx.font.render("BRAK AMUNICJI! Kliknij dowolne pole, by pominąć turę.", True, gfx.PURPLE)
            self.screen.blit(msg, (gfx.WIDTH//2 - msg.get_width()//2, 60))
            
            if self.eco.bombardments > 0:
                mode_text = "WYŁĄCZ BOMBARDOWANIE" if self.bomb_mode else "UŻYJ BOMBARDOWANIA"
                color = gfx.ORANGE if self.bomb_mode else gfx.GRAY
                gfx.draw_button(self.screen, self.bomb_toggle_btn_rect, mode_text, color)
            
        elif self.game_phase == 'SHOP':
            msg = gfx.font.render("FAZA ZAKUPÓW: Ulepsz flotę przed ruchem", True, gfx.GREEN)
            self.screen.blit(msg, (gfx.WIDTH//2 - msg.get_width()//2, 60))
            
            alive = sum(1 for ship in self.player_ships if not ship.is_sunk())
            if alive == 1:
                lc_msg = gfx.font.render("LAST CHANCE AKTYWNE: -80% na ceny!", True, gfx.PURPLE)
                self.screen.blit(lc_msg, (gfx.WIDTH//2 - lc_msg.get_width()//2, 510))

            ammo_price = self.eco.get_price('ammo', alive)
            repair_price = self.eco.get_price('repair', alive)
            bomb_price = self.eco.get_price('bomb', alive)
            ref_price = self.eco.get_price('refinery', alive)
            
            gfx.draw_button(self.screen, self.buy_ammo_btn_rect, f"Amunicja (+10) - {ammo_price} CR", gfx.GREEN if self.eco.credits >= ammo_price else gfx.GRAY)
            gfx.draw_button(self.screen, self.buy_repair_btn_rect, f"Naprawa (1 HP) - {repair_price} CR", gfx.GREEN if self.eco.credits >= repair_price else gfx.GRAY)
            gfx.draw_button(self.screen, self.buy_bomb_btn_rect, f"Nalot 2x5 - {bomb_price} CR", gfx.ORANGE if self.eco.credits >= bomb_price else gfx.GRAY)
            
            has_ref = any(s.is_refinery and not s.is_sunk() for s in self.player_ships)
            if has_ref:
                gfx.draw_button(self.screen, self.buy_refinery_btn_rect, "RAFINERIA AKTYWNA", gfx.DARK_GREEN)
            else:
                gfx.draw_button(self.screen, self.buy_refinery_btn_rect, f"Rafineria (+50/t) - {ref_price} CR", gfx.DARK_GREEN if self.eco.credits >= ref_price else gfx.GRAY)
                
            gfx.draw_button(self.screen, self.action_btn_rect, "ZAKOŃCZ ZAKUPY", gfx.YELLOW)
            
        elif self.game_phase == 'MOVE':
            msg = gfx.font.render("FAZA RUCHU: Wykonaj manewr floty lub złap Złoty Skarb!", True, gfx.YELLOW)
            self.screen.blit(msg, (gfx.WIDTH//2 - msg.get_width()//2, 60))
            gfx.draw_button(self.screen, self.action_btn_rect, "WYKONAJ RUCH", gfx.YELLOW)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_mouse_click(event.pos)
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = BattleshipGame()
    game.run()
