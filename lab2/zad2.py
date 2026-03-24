import pygame

pygame.init()

WIN_W, WIN_H = 600, 600
win = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("zad 2")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(WHITE)

    cx_tl, cy_tl = 150, 150
    circle_r = 100
    pygame.draw.circle(win, BLACK, (cx_tl, cy_tl), circle_r)

    square_size = 100
    square_x = cx_tl - square_size // 2
    square_y = cy_tl - square_size // 2
    pygame.draw.rect(win, YELLOW, (square_x, square_y, square_size, square_size))

    green_points = [
        (350, 50),
        (550, 50),
        (550, 250),
        (450, 150),
        (350, 250)
    ]
    pygame.draw.polygon(win, GREEN, green_points)

    pygame.draw.polygon(win, BLUE, [(105, 340), (195, 340), (150, 410)])
    pygame.draw.rect(win, BLUE, (70, 410, 160, 70))
    pygame.draw.polygon(win, BLUE, [(105, 550), (195, 550), (150, 480)])

    red_points = [
        (350, 360),
        (550, 360),
        (350, 540),
        (550, 540)
    ]
    pygame.draw.lines(win, RED, False, red_points, 15)

    pygame.draw.rect(win, BLACK, (0, 0, WIN_W, WIN_H), 10)

    pygame.display.update()

pygame.quit()