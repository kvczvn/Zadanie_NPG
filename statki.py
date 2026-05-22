import pygame
import sys
import graphics as gfx
from objects import Ship, Treasure
from economy import Economy
from logic import GameLogic

class BattleshipGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((gfx.WIDTH, gfx.HEIGHT))
        pygame.display.set_caption("Projekt Statki - Zespół NPG")
        self.clock = pygame.time.Clock()

        self.player_ships = []      # Lista na obiekty Ship gracza
        self.computer_ships = []    # Lista na obiekty Ship komputera
        self.player_misses = set()  # Zbiór współrzędnych pudeł gracza
        self.computer_misses = set()# Zbiór współrzędnych pudeł komputera
        
        # Inicjalizacja klas reszty zespołu
        self.eco = Economy() 
        self.treasure = Treasure(gfx.GRID_SIZE)
        
        # Zmienne do zarządzania grą
        self.game_phase = 'SETUP' 
        self.game_over = False
        self.winner_text = ""

    def check_win_conditions(self):
        """Sprawdza, czy któraś z flot została całkowicie zniszczona."""
        # Wygrywasz, jeśli komputer ma statki i WSZYSTKIE (all) zatonęły
        if len(self.computer_ships) > 0 and all(ship.is_sunk() for ship in self.computer_ships):
            self.game_over = True
            self.winner_text = "Wygrałeś! Zniszczyłeś flotę komputera!"
  
    def handle_mouse_click(self, pos):
        """Zamienia kliknięcie myszką na logikę gry zależnie od fazy."""
        if self.game_over: return
        x, y = pos

        # FAZA 1: ROZSTAWIENIE
        if self.game_phase == 'SETUP':
            if gfx.P1_OFFSET_X <= x <= gfx.P1_OFFSET_X + gfx.GRID_SIZE * gfx.CELL_SIZE and \
               gfx.P1_OFFSET_Y <= y <= gfx.P1_OFFSET_Y + gfx.GRID_SIZE * gfx.CELL_SIZE:
                
                c = (x - gfx.P1_OFFSET_X) // gfx.CELL_SIZE
                r = (y - gfx.P1_OFFSET_Y) // gfx.CELL_SIZE
                print(f"Rozstawianie -> Wiersz: {r}, Kolumna: {c}")
                # Kiedy dodacie logikę Małgosi, tutaj wywołasz wstawianie statku
                # Na razie po jednym kliknięciu wymusimy testowo przejście do strzelania:
                self.game_phase = 'SHOOT'

        # FAZA 2: STRZELANIE (Task #22)
        elif self.game_phase == 'SHOOT':
            # Sprawdzamy, czy gracz kliknął w planszę KOMPUTERA (używamy P2_OFFSET)
            if gfx.P2_OFFSET_X <= x <= gfx.P2_OFFSET_X + gfx.GRID_SIZE * gfx.CELL_SIZE and \
               gfx.P2_OFFSET_Y <= y <= gfx.P2_OFFSET_Y + gfx.GRID_SIZE * gfx.CELL_SIZE:
                
                c = (x - gfx.P2_OFFSET_X) // gfx.CELL_SIZE
                r = (y - gfx.P2_OFFSET_Y) // gfx.CELL_SIZE
                
                # --- LOGIKA AMUNICJI ---
                if self.eco.ammo <= 0:
                    print("Brak amunicji! Tracisz turę.")
                else:
                    self.eco.ammo -= 1  # Pobieramy 1 pocisk
                    self.apply_player_shot(r, c) # Oddajemy strzał
                
                # Po strzale sprawdzamy, czy komputer został zniszczony
                self.check_win_conditions()
                
                # Jeśli gra trwa dalej, oddajemy turę komputerowi
                if not self.game_over:
                    GameLogic.computer_shoot(self.player_ships, self.player_misses, gfx.GRID_SIZE)
                    self.check_win_conditions()
                    
                    # Jeśli komputer nas nie zniszczył, idziemy do sklepu
                    if not self.game_over:
                        self.game_phase = 'SHOP'

    # === NOWA FUNKCJA DO STRZELANIA ===
    def apply_player_shot(self, r, c):
        """Sprawdza trafienie, odejmuje HP wrogim statkom i przyznaje nagrody."""
        if (r, c) in self.computer_misses: 
            return # Nie strzelamy dwa razy w to samo pudło
            
        for ship in self.computer_ships:
            if (r, c) in ship.cells:
                idx = ship.cells.index((r, c))
                if not ship.health[idx]: 
                    return # Maszt już jest zniszczony
                    
                was_sunk = ship.is_sunk()
                ship.health[idx] = False # Niszczymy maszt
                self.eco.credits += 50   # Nagroda za trafienie
                
                if not was_sunk and ship.is_sunk():
                    self.eco.credits += 150 # Bonus za zatopienie całego statku
                return 
                
        # Jeśli pętla nie znalazła statku na tych kordach, oznacza to pudło
        self.computer_misses.add((r, c))

    def draw(self):
        """Funkcja rysująca wszystko na ekranie."""
        self.screen.fill(gfx.BG_COLOR)
        
        # W przyszłości tu będą wywoływane funkcje rysujące
        gfx.draw_board_skeleton(self.screen)

        if self.game_over:
            # Jeśli w tekście jest słowo "Wygrałeś", użyj zielonego koloru z pliku grafiki. W przeciwnym razie czerwonego.
            color = gfx.GREEN if "Wygrałeś" in self.winner_text else gfx.RED
            msg = gfx.title_font.render(self.winner_text, True, color)
            # Rysujemy tekst na środku ekranu
            self.screen.blit(msg, (gfx.WIDTH//2 - msg.get_width()//2, gfx.HEIGHT//2))
        
        pygame.display.flip()

    def run(self):
        """Główna pętla gry (Game Loop)."""
        running = True
        while running:
            # Nasłuchiwanie na wydarzenia (np. kliknięcie krzyżyka)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # === TUTAJ WYWOŁUJEMY TWOJĄ FUNKCJĘ PRZELICZAJĄCĄ ===
                    self.handle_mouse_click(event.pos)
            if not self.game_over:
                self.check_win_conditions()

            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = BattleshipGame()
    game.run()
