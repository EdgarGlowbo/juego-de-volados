from os import path

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYGROUND_ASPECT_RATIO = 1600 / 1200
PLAYGROUND_HEIGHT = 320
PLAYGROUND_WIDTH = PLAYGROUND_HEIGHT * PLAYGROUND_ASPECT_RATIO


# Dimensiones imágenes
SALDO_IMG_DIMENSIONS = 64
APUESTA_IMG_DIMENSIONS = 64
RESET_IMG_DIMENSIONS = 64
RESULT_IMG_DIMENSIONS = 400
PLACE_BET_DIMENSIONS = 128

current_dir = path.dirname(path.abspath(__file__))

SALDO_IMG_PATH = path.join(current_dir, "assets/saldo.png")
APUESTA_IMG_PATH = path.join(current_dir, "assets/recompensa.png")
RESET_IMG_PATH = path.join(current_dir, "assets/reset.png")
CARA_PATH = path.join(current_dir, "assets/cara.png")
SELLO_PATH = path.join(current_dir, "assets/sello.png")
PLAYGROUND_START_PATH = path.join(current_dir, "assets/start.png")
