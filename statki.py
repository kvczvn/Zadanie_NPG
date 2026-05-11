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
        
        # Inicjalizacja klas reszty zespołu
        self.eco = Economy() 
        self.treasure = Treasure(gfx.GRID_SIZE)
        
        # Zmienne do zarządzania grą
        self.game_phase = 'SETUP' 
        self.game_over = False

    def draw(self):
        """Funkcja rysująca wszystko na ekranie."""
        self.screen.fill(gfx.BG_COLOR)
        
        # W przyszłości tu będą wywoływane funkcje rysujące
        gfx.draw_board_skeleton(self.screen)
        
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
                    # obsługa kliknięć
                    print("Kliknięto myszką w pozycję:", event.pos)

            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = BattleshipGame()
    game.run()
