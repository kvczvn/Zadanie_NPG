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

    # === TUTAJ ZNAJDUJE SIĘ ROZWIĄZANIE TASKU #10 ===
    def handle_mouse_click(self, pos):
        """Zamienia kliknięcie myszką na współrzędne siatki (wiersz i kolumnę)."""
        if self.game_over: return
        x, y = pos

        if self.game_phase == 'SETUP':
            # Sprawdzamy, czy kliknięcie myszką mieści się w granicach planszy gracza
            if gfx.P1_OFFSET_X <= x <= gfx.P1_OFFSET_X + gfx.GRID_SIZE * gfx.CELL_SIZE and \
               gfx.P1_OFFSET_Y <= y <= gfx.P1_OFFSET_Y + gfx.GRID_SIZE * gfx.CELL_SIZE:
                
                # Przeliczanie pikseli na współrzędne siatki (dzielenie całkowite //)
                c = (x - gfx.P1_OFFSET_X) // gfx.CELL_SIZE
                r = (y - gfx.P1_OFFSET_Y) // gfx.CELL_SIZE
                
                print(f"współrzędne siatki -> Wiersz: {r}, Kolumna: {c}")

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
