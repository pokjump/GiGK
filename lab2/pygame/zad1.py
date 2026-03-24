import math
import sys
import pygame

pygame.init()

SCREEN_W, SCREEN_H = 600, 600
MID_X, MID_Y = SCREEN_W // 2, SCREEN_H // 2
BASE_SIZE = 150
SIDES_COUNT = 4
COLORS = {
    "bg": (255, 255, 0),
    "fill": (24, 69, 200),
    "edge": (15, 15, 15),
    "text": (0, 0, 0)
}

def multiply_matrices(m1, m2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            result[i][j] = m1[i][0]*m2[0][j] + m1[i][1]*m2[1][j] + m1[i][2]*m2[2][j]
    return result

def get_rotation(angle_deg):
    r = math.radians(angle_deg)
    return [[math.cos(r), -math.sin(r), 0],
            [math.sin(r),  math.cos(r), 0],
            [          0,            0, 1]]

def get_scale(x, y):
    return [[x, 0, 0],
            [0, y, 0],
            [0, 0, 1]]

def get_shear(x, y):
    return [[1, x, 0],
            [y, 1, 0],
            [0, 0, 1]]

def get_reflect_x():
    return [[1,  0, 0],
            [0, -1, 0],
            [0,  0, 1]]

def apply_transform(x, y, matrix):
    new_x = matrix[0][0] * x + matrix[0][1] * y + matrix[0][2]
    new_y = matrix[1][0] * x + matrix[1][1] * y + matrix[1][2]
    return int(MID_X + new_x), int(MID_Y + new_y)

def generate_shape(sides, size):
    points = []
    offset = -math.pi / 2
    for i in range(sides):
        angle = offset + (2 * math.pi * i) / sides
        points.append((size * math.cos(angle), size * math.sin(angle)))
    return points

def main():
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("zad 1")

    shape_points = generate_shape(SIDES_COUNT, BASE_SIZE)

    moves = {
        pygame.K_1: get_scale(0.35, 0.35),
        pygame.K_2: multiply_matrices(get_rotation(44), get_scale(0.62, 0.62)),
        pygame.K_3: multiply_matrices(get_reflect_x(), get_scale(0.34, 0.78)),
        pygame.K_4: multiply_matrices(get_shear(-0.32, 0.0), get_scale(0.86, 0.74)),
        pygame.K_5: get_scale(0.92, 0.24),
        pygame.K_6: multiply_matrices(get_shear(0.52, 0.0), get_scale(0.36, 0.90)),
        pygame.K_7: get_scale(0.34, 0.78),
        pygame.K_8: multiply_matrices(get_rotation(-28), get_scale(0.86, 0.30)),
        pygame.K_9: multiply_matrices(multiply_matrices(get_shear(0.12, 0.0), get_reflect_x()), get_scale(1.06, 0.40)),
    }

    active_matrix = moves[pygame.K_1]
    sys_font = pygame.font.SysFont("consolas", 18)
    fps_clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in moves:
                active_matrix = moves[event.key]

        screen.fill(COLORS["bg"])

        drawn_points = [apply_transform(px, py, active_matrix) for px, py in shape_points]

        pygame.draw.polygon(screen, COLORS["fill"], drawn_points)
        pygame.draw.polygon(screen, COLORS["edge"], drawn_points, 3)

        pygame.display.flip()
        fps_clock.tick(60)

if __name__ == "__main__":
    main()