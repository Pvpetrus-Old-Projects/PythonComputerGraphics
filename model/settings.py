import pygame

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 400

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 100

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

BUTTON_Y = HEIGHT - TOOLBAR_HEIGHT / 2 - 25

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint +")


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
