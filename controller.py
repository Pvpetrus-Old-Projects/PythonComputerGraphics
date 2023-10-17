import pygame.draw

from model import *
from view import init_grid, get_row_col_from_pos, draw

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint +")

running = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
current_drawing_mode = "DOT"
start_pos_x = None
start_pos_y = None
end_pos_x = None
end_pos_y = None

button_y = HEIGHT - TOOLBAR_HEIGHT / 2 - 25
buttons = [
    Button(10, button_y, 100, 50, BLACK, "LINE", WHITE),
    Button(120, button_y, 100, 50, BLACK, "DOT", WHITE),
    Button(230, button_y, 100, 50, BLACK, "TEXT", WHITE),
]

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pass

        elif event.type == pygame.MOUSEMOTION:
            pass


        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                # Clicking on drawing space
                # Check drawing mode and choose actions accordingly
                if current_drawing_mode == "DOT":
                    start_pos_x = None
                    start_pos_y = None
                    end_pos_x = None
                    end_pos_y = None
                    row, col = get_row_col_from_pos(pos)
                    grid[row][col] = drawing_color
                if current_drawing_mode == "LINE":
                    row, col = get_row_col_from_pos(pos)
                    if start_pos_x is not None:
                        end_pos_x = col
                        end_pos_y = row
                        middle_pos_x = col + 15
                        middle_pos_y = row
                        pygame.draw.line(WIN, BLUE, (start_pos_x * PIXEL_SIZE, start_pos_y * PIXEL_SIZE),
                                         (end_pos_x * PIXEL_SIZE, end_pos_y * PIXEL_SIZE), 5)
                        pygame.draw.ellipse(WIN, BLUE, (start_pos_x * PIXEL_SIZE, start_pos_y * PIXEL_SIZE,
                                                        end_pos_x * PIXEL_SIZE, end_pos_y * PIXEL_SIZE), 5)
                        pygame.draw.rect(WIN, BLUE, (start_pos_x * PIXEL_SIZE, start_pos_y * PIXEL_SIZE,
                                                     end_pos_x * PIXEL_SIZE, end_pos_y * PIXEL_SIZE), 5)
                        pygame.draw.polygon(WIN, BLUE, ((start_pos_x * PIXEL_SIZE, start_pos_y * PIXEL_SIZE),
                                                        (middle_pos_x * PIXEL_SIZE, middle_pos_y * PIXEL_SIZE),
                                                        (end_pos_x * PIXEL_SIZE, end_pos_y * PIXEL_SIZE)), 5)
                        pygame.display.flip()
                        pygame.display.update()
                    else:
                        start_pos_x = col
                        start_pos_y = row
                if current_drawing_mode == "TEXT":
                    start_pos_x = None
                    start_pos_y = None
                    end_pos_x = None
                    end_pos_y = None
                    row, col = get_row_col_from_pos(pos)
            except IndexError:
                # Clicking on toolbar space
                for button in buttons:
                    if not button.clicked(pos):
                        button.color = BLACK
                        continue
                    button.color = GREEN
                    # Choosing current operation type
                    if button.text == "DOT":
                        current_drawing_mode = "DOT"
                    if button.text == "LINE":
                        current_drawing_mode = "LINE"
                    if button.text == "TEXT":
                        current_drawing_mode = "TEXT"
        draw(WIN, grid, buttons)

rect = pygame.Rect(0, 0, 600, 600)
sub = WIN.subsurface(rect)
pygame.image.save(sub, "screenshot.jpeg")
pygame.quit()
