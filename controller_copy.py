import pygame.draw

from model import *
from view import *

running = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
current_drawing_mode = "DO"
start_pos_x = None
start_pos_y = None
end_pos_x = None
end_pos_y = None
text = ""

buttons = [
    Button(10, BUTTON_Y, 50, 50, BLACK, "LI", WHITE),
    Button(70, BUTTON_Y, 50, 50, BLACK, "DO", WHITE),
    Button(130, BUTTON_Y, 50, 50, BLACK, "TE", WHITE),
    Button(190, BUTTON_Y, 50, 50, BLACK, "TR", WHITE),
    Button(250, BUTTON_Y, 50, 50, BLACK, "EL", WHITE),
    Button(310, BUTTON_Y, 50, 50, BLACK, "RE", WHITE),
]

WIN.fill(BG_COLOR)

input_rect = pygame.Rect(370, BUTTON_Y, 140, 50)

color_textbox = pygame.Color('lightskyblue3')

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

        if event.type == pygame.KEYDOWN:

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                text = text[:-1]

                # Unicode standard is used for string
            # formation
            else:
                text += event.unicode

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                # Clicking on drawing space
                # Check drawing mode and choose actions accordingly
                if current_drawing_mode == "DO":
                    start_pos_x = None
                    start_pos_y = None
                    end_pos_x = None
                    end_pos_y = None
                    row, col = get_row_col_from_pos(pos)
                    WIN.fill(BLUE, ((col * PIXEL_SIZE, row * PIXEL_SIZE), (PIXEL_SIZE, PIXEL_SIZE)))
                    pygame.display.flip()
                    pygame.display.update()
                if current_drawing_mode == "LI":
                    row, col = get_row_col_from_pos(pos)
                    if start_pos_x is not None:
                        end_pos_x = col
                        end_pos_y = row
                        middle_pos_x = col + 15
                        middle_pos_y = row
                        draw_line(WIN, BLACK, start_pos_x, start_pos_y, end_pos_x, end_pos_y)
                        pygame.display.flip()
                        pygame.display.update()
                        start_pos_x = None
                        start_pos_y = None
                    else:
                        start_pos_x = col
                        start_pos_y = row
                if current_drawing_mode == "TR":
                    row, col = get_row_col_from_pos(pos)
                    if start_pos_x is not None:
                        end_pos_x = col
                        end_pos_y = row
                        middle_pos_x = col + 15
                        middle_pos_y = row
                        draw_polygon(WIN, BLACK, start_pos_x, start_pos_y, middle_pos_x, middle_pos_y, end_pos_x, end_pos_y)
                        pygame.display.flip()
                        pygame.display.update()
                        start_pos_x = None
                        start_pos_y = None
                    else:
                        start_pos_x = col
                        start_pos_y = row
                if current_drawing_mode == "EL":
                    row, col = get_row_col_from_pos(pos)
                    if start_pos_x is not None:
                        end_pos_x = col
                        end_pos_y = row
                        middle_pos_x = col + 15
                        middle_pos_y = row
                        # TODO rozmiar zamiast pozycji końcowej?
                        draw_ellipse(WIN, BLACK, start_pos_x, start_pos_y, end_pos_x, end_pos_y)
                        pygame.display.flip()
                        pygame.display.update()
                        start_pos_x = None
                        start_pos_y = None
                    else:
                        start_pos_x = col
                        start_pos_y = row
                if current_drawing_mode == "RE":
                    row, col = get_row_col_from_pos(pos)
                    if start_pos_x is not None:
                        end_pos_x = col
                        end_pos_y = row
                        middle_pos_x = col + 15
                        middle_pos_y = row
                        draw_rect(WIN, BLACK, start_pos_x, start_pos_y, end_pos_x, end_pos_y)
                        pygame.display.flip()
                        pygame.display.update()
                        start_pos_x = None
                        start_pos_y = None
                    else:
                        start_pos_x = col
                        start_pos_y = row
                if current_drawing_mode == "TE":
                    start_pos_x = None
                    start_pos_y = None
                    end_pos_x = None
                    end_pos_y = None
                    row, col = get_row_col_from_pos(pos)
                    button_font = get_font(22)
                    text_surface = button_font.render(text, 1, BLUE)
                    WIN.blit(text_surface, (col * PIXEL_SIZE, row * PIXEL_SIZE))

            except IndexError:
                # Clicking on toolbar space
                button_clicked = False
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    button_clicked = True
                    button.color = GREEN
                    # Choosing current operation type
                    if button.text == "DO":
                        current_drawing_mode = "DO"
                    if button.text == "LI":
                        current_drawing_mode = "LI"
                    if button.text == "TE":
                        current_drawing_mode = "TE"
                    if button.text == "TR":
                        current_drawing_mode = "TR"
                    if button.text == "EL":
                        current_drawing_mode = "EL"
                    if button.text == "RE":
                        current_drawing_mode = "RE"
                if button_clicked:
                    for button in buttons:
                        if not button.clicked(pos):
                            button.color = BLACK

        pygame.draw.rect(WIN, color_textbox, input_rect)

        text_surface = get_font(22).render(text, True, (255, 255, 255))

        # render at position stated in arguments
        WIN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

    draw(WIN, buttons)

rect = pygame.Rect(0, 0, 600, 600)
sub = WIN.subsurface(rect)
pygame.image.save(sub, "screenshot.jpeg")
pygame.quit()
