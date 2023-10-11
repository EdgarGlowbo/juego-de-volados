import pygame
from game import Game
from scoreboard import Scoreboard

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de volados")
game = Game(screen)


# Loop principal
while game.running:
    game.handle_events()
    game.render()

pygame.quit()
