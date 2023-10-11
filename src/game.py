import os
import sys
import pygame
import random
from coin import Coin
from scoreboard import Scoreboard

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(root_dir)
from settings import (
    PLAYGROUND_START_PATH,
    PLACE_BET_DIMENSIONS,
    PLAYGROUND_HEIGHT,
    PLAYGROUND_WIDTH,
)


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.coin = Coin()
        self.scoreboard = Scoreboard()
        self.font = pygame.font.Font(None, 36)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.rect_cara.collidepoint(pos):
                    self.make_bet("cara")
                elif self.rect_sello.collidepoint(pos):
                    self.make_bet("sello")

    def make_bet(self, choice):
        result = random.choice(["cara", "sello"])

        if self.scoreboard.saldo >= self.scoreboard.apuesta:
            self.play_animation(self.screen)
            if result == choice:
                self.scoreboard.saldo += self.scoreboard.apuesta
                self.scoreboard.apuesta = 10
                self.coin.draw_result(self.screen, result, "¡Ganaste!")

            else:
                self.scoreboard.saldo -= self.scoreboard.apuesta
                self.scoreboard.apuesta *= 2
                self.coin.draw_result(self.screen, result, "¡Perdiste!")

            # condiciones especiales
            if self.scoreboard.saldo < self.scoreboard.apuesta:
                self.scoreboard.apuesta = self.scoreboard.saldo
            if self.scoreboard.saldo == 0:
                self.draw_game_over()
            if self.scoreboard.saldo >= self.scoreboard.recompensa_maxima:
                self.draw_game_over()

    def render_text(self, text, color):
        return self.font.render(text, True, color)

    def draw_place_bet_btns(self, screen):
        self.coin.sello_img = pygame.transform.scale(
            self.coin.sello_img, (PLACE_BET_DIMENSIONS, PLACE_BET_DIMENSIONS)
        )
        self.coin.cara_img = pygame.transform.scale(
            self.coin.cara_img, (PLACE_BET_DIMENSIONS, PLACE_BET_DIMENSIONS)
        )
        total_width = (
            self.coin.cara_img.get_width() + self.coin.sello_img.get_width() + 50
        )
        x_position = (screen.get_width() - total_width) // 2

        center_x = x_position + self.coin.cara_img.get_width() + 25

        screen.blit(self.coin.cara_img, (x_position, 100))
        screen.blit(
            self.coin.sello_img,
            (x_position + self.coin.cara_img.get_width() + 50, 100),
        )

        text_surface = self.render_text("¿Qué apuestas?", self.BLACK)
        text_rect = text_surface.get_rect(center=(center_x, 30))
        self.rect_cara = pygame.Rect(
            x_position,
            100,
            self.coin.cara_img.get_width(),
            self.coin.cara_img.get_height(),
        )
        self.rect_sello = pygame.Rect(
            x_position + self.coin.cara_img.get_width(),
            100,
            self.coin.sello_img.get_width(),
            self.coin.sello_img.get_height(),
        )
        screen.blit(text_surface, text_rect)

    def draw_playground(self, screen, playground_image):
        playground_image = pygame.transform.scale(
            playground_image, (PLAYGROUND_WIDTH, PLAYGROUND_HEIGHT)
        )

        x_position = (screen.get_width() - playground_image.get_width()) // 2
        y_position = screen.get_height() - playground_image.get_height()

        screen.blit(playground_image, (x_position, y_position))

    def play_animation(self, screen):
        animation_folder = "coin_flip_frames/"
        animation_frames = []

        for i in range(1, 53):
            frame_path = os.path.join(
                "..", "assets", animation_folder, f"coin_flip_{i}.png"
            )
            frame = pygame.image.load(frame_path)
            animation_frames.append(frame)

        for frame in animation_frames:
            self.draw_playground(screen, frame)
            pygame.display.flip()
            pygame.time.delay(50)

    def draw_game_over(self):
        self.scoreboard.reiniciar_scoreboard()
        self.screen.fill(self.WHITE)
        text_surface = self.render_text("Game Over", self.BLACK)
        text_rect = text_surface.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
        )

        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        self.render()

    def render(self):
        self.screen.fill((255, 255, 255))

        # Tablero
        self.scoreboard.draw_scoreboard(self.screen)
        # Reiniciar
        # self.scoreboard.draw_reset(self.screen)

        # Botones para apostar cara o sello
        self.draw_place_bet_btns(self.screen)

        # Área principal inicial
        self.draw_playground(self.screen, pygame.image.load(PLAYGROUND_START_PATH))

        pygame.display.flip()
