import pygame, sys
from settings import *

pygame.init()
clock = pygame.time.Clock()

# screen
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((98, 98, 98))

# player 1
player_1 = pygame.Surface((15,100))
player_1_rect = player_1.get_rect(topleft=(0, 300))
player_1.fill('blue')

# player 2
player_2 = pygame.Surface((15,100))
player_2_rect = player_2.get_rect(topright=(1200, 300))
player_2.fill('red')


# ball
ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect(midleft=(585, 325))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(player_1, player_1_rect)
    screen.blit(player_2, player_2_rect)
    screen.blit(ball, ball_rect)

    pygame.draw.line(screen, "white", (screen_width / 2, 0) , (screen_width / 2, screen_height))

    pygame.display.update()
    clock.tick(framerate)