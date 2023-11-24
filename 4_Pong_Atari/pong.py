import pygame
import random
from math import sqrt

# do poprawienia:

pygame.font.init()

PLAY_FONT = pygame.font.SysFont('comicsans', 100)
SCORE_FONT = pygame.font.SysFont('comicsans', 60)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
COUNTDOWN_FONT = pygame.font.SysFont('comicsans', 30)


WIDTH, HEIGHT = 1080, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER_WIDTH = 5
BORDER = pygame.Rect(WIDTH//2-BORDER_WIDTH//2, 0, BORDER_WIDTH, HEIGHT)

RACKET_WIDTH, RACKET_HEIGHT = 10, 100
BALL_SIZE = 10

RACKET_VELOCITY = 6

ball_y_velocity = 8
ball_x_velocity = 8
BALL_VEL_SQUARED = ball_x_velocity**2+ball_y_velocity**2
CONST_BALL_VEL = sqrt(BALL_VEL_SQUARED)

FPS = 60

MAX_SCORE = 21

# BONUS_TIME = FPS*30 #seconds

PLAYER1_SCORED = pygame.USEREVENT + 1
PLAYER2_SCORED = pygame.USEREVENT + 2


def changeDirection():
    return random.randint(0, 1)


def randomlyStartTheBall(ball):
    global ball_x_velocity
    global ball_y_velocity

    ball_y_velocity = 5
    ball_x_velocity = sqrt(BALL_VEL_SQUARED - ball_y_velocity**2)

    ball.x = WIDTH//2-BALL_SIZE//2
    start_on_top = random.randint(0, 1)
    switch_direction = random.randint(0, 1)

    if start_on_top:
        ball.y = 3
    else:
        ball.y = HEIGHT - BALL_SIZE - 3

    if switch_direction:
        ball_x_velocity *= -1


def printWindow(player1, player2, ball, player1_score, player2_score):

    WINDOW.fill(BLACK)

    pygame.draw.rect(WINDOW, WHITE, player1)
    pygame.draw.rect(WINDOW, WHITE, player2)
    pygame.draw.rect(WINDOW, WHITE, ball)

    player1_score_text = SCORE_FONT.render(str(player1_score), 1, WHITE)
    player2_score_text = SCORE_FONT.render(str(player2_score), 1, WHITE)

    pygame.draw.rect(WINDOW, WHITE, BORDER)
    WINDOW.blit(player1_score_text, (WIDTH//4 -
                player1_score_text.get_width(), 15))
    WINDOW.blit(player2_score_text, ((WIDTH//4)*3, 15))
    pygame.display.update()


def player1Movement(key_pressed, player1):
    if key_pressed[pygame.K_w] and player1.y - RACKET_VELOCITY > -1:  # up
        player1.y -= RACKET_VELOCITY
    if key_pressed[pygame.K_s] and player1.y + RACKET_VELOCITY < HEIGHT-RACKET_HEIGHT:  # down
        player1.y += RACKET_VELOCITY


def player2Movement(key_pressed, player2):
    if key_pressed[pygame.K_UP] and player2.y - RACKET_VELOCITY > -1:  # up
        player2.y -= RACKET_VELOCITY
    if key_pressed[pygame.K_DOWN] and player2.y + RACKET_VELOCITY < HEIGHT-RACKET_HEIGHT:  # down
        player2.y += RACKET_VELOCITY


def ballMovement(key_pressed, ball, player1, player2):
    global ball_x_velocity
    global ball_y_velocity

    ball.y += ball_y_velocity
    ball.x += ball_x_velocity

    if ball.y <= 2 or ball.y >= HEIGHT-BALL_SIZE-2:  # hits top or bottom wall
        ball_y_velocity *= -1

    if ball.x <= -10:  # hits left wall
        pygame.event.post(pygame.event.Event(PLAYER2_SCORED))
        randomlyStartTheBall(ball)

    if ball.x >= WIDTH+5:  # hits right wall
        pygame.event.post(pygame.event.Event(PLAYER1_SCORED))
        randomlyStartTheBall(ball)

    if ball.colliderect(player1):  # colides  with left paddle
        if player1.y + 48 <= ball.y+BALL_SIZE//2 <= player1.y + 52:
            ball_y_velocity = 0
            ball_x_velocity = CONST_BALL_VEL

        elif (player1.y + 12 <= ball.y+BALL_SIZE//2 < player1.y + 24) or (player1.y + 76 < ball.y+BALL_SIZE//2 <= player1.y + 88):
            if ball_y_velocity >= 0:
                ball_y_velocity = 6
            else:
                ball_y_velocity = -6
            ball_x_velocity = sqrt(BALL_VEL_SQUARED - ball_y_velocity**2)

        elif (player1.y + 24 <= ball.y+BALL_SIZE//2 < player1.y + 36) or (player1.y + 64 < ball.y+BALL_SIZE//2 <= player1.y + 76):
            if ball_y_velocity >= 0:
                ball_y_velocity = 4
            else:
                ball_y_velocity = -4
            ball_x_velocity = sqrt(BALL_VEL_SQUARED - ball_y_velocity**2)

        elif (player1.y + 36 <= ball.y+BALL_SIZE//2 < player1.y + 48) or (player1.y + 52 < ball.y+BALL_SIZE//2 <= player1.y + 64):
            if ball_y_velocity >= 0:
                ball_y_velocity = 2
            else:
                ball_y_velocity = -2
            ball_x_velocity = sqrt(BALL_VEL_SQUARED - ball_y_velocity**2)

        else:
            if ball_y_velocity >= 0:
                ball_y_velocity = 8
            else:
                ball_y_velocity = -8
            ball_x_velocity = 8

        if (key_pressed[pygame.K_w] and ball_y_velocity > 0) or (key_pressed[pygame.K_s] and ball_y_velocity < 0):
            ball_y_velocity *= -1

    if ball.colliderect(player2):  # colides with right paddle
        if player2.y + 48 <= ball.y+BALL_SIZE//2 <= player2.y + 52:
            ball_y_velocity = 0
            ball_x_velocity = -CONST_BALL_VEL

        elif (player2.y + 12 <= ball.y+BALL_SIZE//2 < player2.y + 24) or (player2.y + 76 < ball.y+BALL_SIZE//2 <= player2.y + 88):
            if ball_y_velocity >= 0:
                ball_y_velocity = 6
            else:
                ball_y_velocity = -6
            ball_x_velocity = -sqrt(BALL_VEL_SQUARED - ball_y_velocity**2)

        elif (player2.y + 24 <= ball.y+BALL_SIZE//2 < player2.y + 36) or (player2.y + 64 < ball.y+BALL_SIZE//2 <= player2.y + 76):
            if ball_y_velocity >= 0:
                ball_y_velocity = 4
            else:
                ball_y_velocity = -4
            ball_x_velocity = -sqrt(BALL_VEL_SQUARED - ball_y_velocity**2)

        elif (player2.y + 36 <= ball.y+BALL_SIZE//2 < player2.y + 48) or (player2.y + 52 < ball.y+BALL_SIZE//2 <= player2.y + 64):
            if ball_y_velocity >= 0:
                ball_y_velocity = 2
            else:
                ball_y_velocity = -2
            ball_x_velocity = -sqrt(BALL_VEL_SQUARED - ball_y_velocity**2)

        else:
            if ball_y_velocity >= 0:
                ball_y_velocity = 8
            else:
                ball_y_velocity = -8
            ball_x_velocity = -8

        if (key_pressed[pygame.K_UP] and ball_y_velocity > 0) or (key_pressed[pygame.K_DOWN] and ball_y_velocity < 0):
            ball_y_velocity *= -1


def handleBonuses():
    pass


def printWinner(text):
    winner_text = WINNER_FONT.render(text, 1, WHITE)
    WINDOW.blit(winner_text, (WIDTH//2 - winner_text.get_width() //
                2, HEIGHT//2 - winner_text.get_height()//2))

    pygame.display.update()
    pygame.time.delay(2000)


def main():

    player1 = pygame.Rect(0, HEIGHT//2 - RACKET_HEIGHT //
                          2, RACKET_WIDTH, RACKET_HEIGHT)
    player2 = pygame.Rect(WIDTH-RACKET_WIDTH, HEIGHT //
                          2 - RACKET_HEIGHT//2, RACKET_WIDTH, RACKET_HEIGHT)

    player1_score = player2_score = 0

    ball = pygame.Rect(WIDTH//2-BALL_SIZE//2, HEIGHT//2 -
                       BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
    clock = pygame.time.Clock()
    run = True

    winner = ''
    while run:
        clock.tick(FPS)

        if winner != '':
            printWinner(winner)
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == PLAYER1_SCORED:
                player1_score += 1
                pygame.display.update()

            if event.type == PLAYER2_SCORED:
                player2_score += 1
                pygame.display.update()

        key_pressed = pygame.key.get_pressed()
        player1Movement(key_pressed, player1)
        player2Movement(key_pressed, player2)
        ballMovement(key_pressed, ball, player1, player2)
        printWindow(player1, player2, ball, player1_score, player2_score)

        if player1_score == MAX_SCORE:
            winner = "Player1 Won"

        if player2_score == MAX_SCORE:
            winner = "Player2 Won"

    pygame.quit()


if __name__ == "__main__":
    main()
