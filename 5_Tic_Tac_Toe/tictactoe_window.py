import pygame
from pygame.locals import *
import sys
import random
pygame.init()


SIZE = 600
WIN = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("TIC TAC TOE")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

board = {}


def create_board_dict():
    for i in range(1, 4):
        for j in range(1, 4):
            board[(j, i)] = 0


def draw_grid():

    for x in range(SIZE//3, SIZE*2//3 + 1, SIZE//3):
        line1 = pygame.Rect(x-5, 0, 10, SIZE)
        line2 = pygame.Rect(0, x-5, SIZE, 10)
        pygame.draw.rect(WIN, WHITE, line1)
        pygame.draw.rect(WIN, WHITE, line2)


def draw_x(mouse_x, mouse_y):
    x_pos = mouse_x // (SIZE//3) + 1
    y_pos = mouse_y // (SIZE//3) + 1

    point = (x_pos, y_pos)

    if board[point] != 0:
        return "zle"

    pygame.draw.line(WIN, BLUE,
                     ((((2*x_pos) - 1) * SIZE // 6) - SIZE//12,
                      (((2*y_pos) - 1) * SIZE // 6) - SIZE//12),
                     ((((2*x_pos) - 1) * SIZE // 6) + SIZE//12,
                      (((2*y_pos) - 1) * SIZE // 6) + SIZE//12),
                     5)

    pygame.draw.line(WIN, BLUE,
                     ((((2*x_pos) - 1) * SIZE // 6) + SIZE//12,
                      (((2*y_pos) - 1) * SIZE // 6) - SIZE//12),
                     ((((2*x_pos) - 1) * SIZE // 6) - SIZE//12,
                      (((2*y_pos) - 1) * SIZE // 6) + SIZE//12),
                     5)

    board[point] = 1


def draw_o(random_x, random_y):
    x_pos = random_x // (SIZE//3) + 1
    y_pos = random_y // (SIZE//3) + 1

    point = (x_pos, y_pos)

    while board[point] != 0:
        x_pos = random.randint(0, SIZE) // (SIZE//3) + 1
        y_pos = random.randint(0, SIZE) // (SIZE//3) + 1
        point = (x_pos, y_pos)

    pygame.draw.circle(WIN, RED,
                       (((2*x_pos) - 1) * SIZE // 6,
                        ((2*y_pos) - 1) * SIZE // 6),
                       SIZE//12, 5)

    board[point] = -1


def coinflip():
    if random.randint(0, 1):
        print("Zaczyna uzytkownik")
        return True
    print("Zaczyna komputer")
    return False


def checkifwon():

    for i in range(1, 4):
        suma_rzad = suma_kol = 0

        for j in range(1, 4):
            suma_rzad += board[(i, j)]
            suma_kol += board[(j, i)]

        if suma_rzad == 3 or suma_kol == 3:
            return 'U'
        elif suma_rzad == -3 or suma_kol == -3:
            return 'C'

    global suma_przek1
    global suma_przek2

    suma_przek1 = suma_przek2 = 0

    for i in range(1, 4):
        for j in range(1, 4):
            if i == j:
                suma_przek1 += board[(i, j)]
            if i+j == 4:
                suma_przek2 += board[(i, j)]

    if suma_przek1 == 3 or suma_przek2 == 3:
        return 'U'
    elif suma_przek1 == -3 or suma_przek2 == -3:
        return 'C'

    return False


def nospace():
    for i in range(1, 4):
        for j in range(1, 4):
            if board[(i, j)] == 0:
                return False
    return True


def main():

    run = True

    clock = pygame.time.Clock()
    FPS = 60

    WIN.fill(BLACK)
    draw_grid()
    pygame.display.update()
    create_board_dict()
    players_turn = coinflip()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and players_turn:
                # playthegame()
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:

                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]

                    if draw_x(mouse_x, mouse_y) != "zle":
                        players_turn = False

                    pygame.display.update()
                    winner = checkifwon()
                    if winner == "U":
                        print("Wygrał uzytkownik!!")
                        pygame.time.delay(2000)
                        run = False
                        pygame.quit()

                    elif nospace():
                        print("Remis")
                        pygame.time.delay(2000)
                        run = False
                        pygame.quit()

            if not players_turn:
                draw_o(random.randint(0, SIZE), random.randint(0, SIZE))
                players_turn = True
                pygame.display.update()
                winner = checkifwon()
                if winner == "C":
                    print("Wygrał komputer:((")
                    pygame.time.delay(2000)
                    run = False
                    pygame.quit()

                elif nospace():
                    print("Remis")
                    pygame.time.delay(2000)
                    run = False
                    pygame.quit()


if __name__ == "__main__":
    main()
