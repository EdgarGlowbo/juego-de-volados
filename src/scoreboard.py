import pygame
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(root_dir)
from settings import (
    SALDO_IMG_PATH,
    APUESTA_IMG_PATH,
    RESET_IMG_PATH,
    SALDO_IMG_DIMENSIONS,
    APUESTA_IMG_DIMENSIONS,
    RESET_IMG_DIMENSIONS,
)


class Scoreboard:
    def __init__(self, saldo=80, apuesta=10, recompensa_maxima=280):
        self.saldo = saldo
        self.apuesta = apuesta
        self.recompensa_maxima = recompensa_maxima
        self.saldo_image = pygame.image.load(SALDO_IMG_PATH)
        self.apuesta_image = pygame.image.load(APUESTA_IMG_PATH)
        self.reset_image = pygame.image.load(RESET_IMG_PATH)
        self.saldo_image = pygame.transform.scale(
            self.saldo_image, (SALDO_IMG_DIMENSIONS, SALDO_IMG_DIMENSIONS)
        )
        self.apuesta_image = pygame.transform.scale(
            self.apuesta_image, (APUESTA_IMG_DIMENSIONS, APUESTA_IMG_DIMENSIONS)
        )
        self.reset_image = pygame.transform.scale(
            self.reset_image, (RESET_IMG_DIMENSIONS, RESET_IMG_DIMENSIONS)
        )
        self.font = pygame.font.Font(None, 36)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

    def reiniciar_scoreboard(self):
        self.saldo = 80
        self.apuesta = 10

    def render_text(self, text, color):
        return self.font.render(text, True, color)

    def draw_scoreboard(self, screen):
        screen.blit(
            self.saldo_image,
            (screen.get_width() - self.saldo_image.get_width() - 10, 10),
        )
        screen.blit(
            self.apuesta_image,
            (screen.get_width() - self.apuesta_image.get_width() - 10, 80),
        )
        screen.blit(
            self.render_text("Saldo: {}".format(self.saldo), self.BLACK),
            (screen.get_width() - 220, 10),
        )
        screen.blit(
            self.render_text("Apuesta: {}".format(self.apuesta), self.BLACK),
            (screen.get_width() - 220, 80),
        )

    def draw_reset(self, screen):
        screen.blit(self.reset_image, (10, 10))
