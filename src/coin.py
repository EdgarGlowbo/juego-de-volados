import pygame
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(root_dir)
from settings import CARA_PATH, SELLO_PATH


class Coin:
    def __init__(self):
        self.cara_img = pygame.image.load(CARA_PATH)
        self.sello_img = pygame.image.load(SELLO_PATH)
        self.font = pygame.font.Font(None, 36)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

    def render_text(self, text, color):
        return self.font.render(text, True, color)

    def draw_result(self, screen, result, text):
        screen.fill(self.WHITE)
        if result == "cara":
            self.result_img = self.cara_img
        else:
            self.result_img = self.sello_img
        x_position = (screen.get_width() - self.result_img.get_width()) // 2
        y_position = (screen.get_height() - self.result_img.get_height()) // 2

        text_surface = self.render_text(text, self.BLACK)
        text_rect = text_surface.get_rect(
            center=(x_position + self.result_img.get_width() // 2, y_position - 30)
        )

        screen.blit(self.result_img, (x_position, y_position))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
