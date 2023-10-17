from model import *


def init_grid(rows, cols, color):
    return [[color for _ in range(cols)] for _ in range(rows)]


def draw(win, buttons):
    for button in buttons:
        button.draw(win)
    pygame.display.update()


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


def draw_polygon(window, color, start_pos_x, start_pos_y, middle_pos_x, middle_pos_y, end_pos_x, end_pos_y):
    pygame.draw.polygon(window, color, ((start_pos_x * PIXEL_SIZE, start_pos_y * PIXEL_SIZE),
                                        (middle_pos_x * PIXEL_SIZE, middle_pos_y * PIXEL_SIZE),
                                        (end_pos_x * PIXEL_SIZE, end_pos_y * PIXEL_SIZE)), 5)


def draw_line(window, color, start_pos_x, start_pos_y, end_pos_x, end_pos_y):
    pygame.draw.line(window, color, (start_pos_x * PIXEL_SIZE, start_pos_y * PIXEL_SIZE),
                     (end_pos_x * PIXEL_SIZE, end_pos_y * PIXEL_SIZE), 5)


def draw_ellipse(window, color, start_pos_x, start_pos_y, end_pos_x, end_pos_y):
    pos_diff_x = abs(start_pos_x - end_pos_x)
    pos_diff_y = abs(start_pos_y - end_pos_y)
    # pos_x = start_pos_x if start_pos_x < end_pos_y else end_pos_y
    # pos_y = start_pos_y if start_pos_y < end_pos_y else end_pos_y
    pygame.draw.ellipse(window, color, (start_pos_x * PIXEL_SIZE, start_pos_y * PIXEL_SIZE,
                                        pos_diff_x * PIXEL_SIZE, pos_diff_y * PIXEL_SIZE), 5)


def draw_rect(window, color, start_pos_x, start_pos_y, end_pos_x, end_pos_y):
    pos_diff_x = abs(start_pos_x - end_pos_x)
    pos_diff_y = abs(start_pos_y - end_pos_y)
    # pos_x = start_pos_x if start_pos_x < end_pos_y else end_pos_y
    # pos_y = start_pos_y if start_pos_y < end_pos_y else end_pos_y
    pygame.draw.rect(window, color, (start_pos_x * PIXEL_SIZE, start_pos_y * PIXEL_SIZE,
                                 pos_diff_x * PIXEL_SIZE, pos_diff_y * PIXEL_SIZE), 5)
