import pygame, sys
from settings import *

pygame.init()
clock = pygame.time.Clock()

# screen
screen = pygame.display.set_mode((screen_width, screen_height))

# ball
ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect(topleft=(screen_width / 2,screen_height / 2))
# player 1
player_1 = pygame.Surface((10, 100))
player_1_rect = player_1.get_rect(topleft=(0, screen_height / 2))
player_1.fill('blue')
# player 2
player_2 = pygame.Surface((10, 100))
player_2_rect = player_1.get_rect(topleft=(screen_width -10, screen_height / 2))
player_2.fill('red')

ball_speed_x = 7
ball_speed_y = 7


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y


    if ball_rect.bottom >= screen_height or ball_rect.top <= 0:
        ball_speed_y *= -1

    if ball_rect.right >= screen_width or ball_rect.left <= 0:
        ball_speed_x *= -1


    screen.fill((98, 98, 98))
    screen.blit(player_1, player_1_rect)
    screen.blit(player_2, player_2_rect)
    screen.blit(ball, ball_rect)
    pygame.draw.line(screen, "white", (screen_width / 2, 0) , (screen_width / 2, screen_height))

    pygame.display.flip()
    clock.tick(60)