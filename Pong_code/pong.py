import pygame, sys
from settings import *

pygame.init()
clock = pygame.time.Clock()

# screen
screen = pygame.display.set_mode((screen_width, screen_height))

# score
player_1_score = 0
player_2_score = 0
font = pygame.font.Font('../font/Roboto-Black.ttf', 100)
win_font = pygame.font.Font('../font/Roboto-Black.ttf', 80)
restart_font = pygame.font.Font('../font/Roboto-Black.ttf', 40)

score_1 = font.render(f'{player_1_score}', True, 'blue')
score_2 = font.render(f'{player_2_score}', True, 'red')

player_1_win = win_font.render('Player 1 Win', True, 'blue')
player_2_win = win_font.render('Player 2 Win', True, 'red')

restart_1 = restart_font.render('Press Space to restart', True, 'red')
restart_2 = restart_font.render('Press Space to restart', True, 'blue')

# ball
ball = pygame.image.load('../images/ball.png')
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

players_speed = 8

game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_active == False:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    player_1_score = 0
                    player_2_score = 0
                    ball_rect.x = screen_width / 2
                    ball_rect.y = screen_height / 2

    # players movements
    pressed = pygame.key.get_pressed()
    # player 2 movements
    if pressed[pygame.K_UP]:
        player_2_rect.y -= players_speed
    if pressed[pygame.K_DOWN]:
        player_2_rect.y += players_speed
    # player 1 movements
    if pressed[pygame.K_w]:
        player_1_rect.y -= players_speed
    if pressed[pygame.K_s]:
        player_1_rect.y += players_speed

    if player_1_rect.bottom >= screen_height:
        player_1_rect.bottom = screen_height
    if player_1_rect.top <= 0:
        player_1_rect.top = 0

    if player_2_rect.bottom >= screen_height:
        player_2_rect.bottom = screen_height
    if player_2_rect.top <= 0:
        player_2_rect.top = 0

    # ball movements
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # collids between ball and players
    if ball_rect.colliderect(player_1_rect):
        ball_speed_x *= -1
    if ball_rect.colliderect(player_2_rect):
        ball_speed_x *= -1


    # collids between ball and wals
    if ball_rect.bottom >= screen_height or ball_rect.top <= 0:
        ball_speed_y *= -1

    if ball_rect.right >= screen_width:
        ball_rect.x = screen_width / 2 - 15
        ball_rect.y = screen_height / 2 - 15
        ball_speed_x *= -1
        player_1_score += 1
    if ball_rect.left <= 0:
        ball_rect.x = screen_width / 2
        ball_rect.y = screen_height / 2
        ball_speed_x *= -1
        player_2_score += 1

    score_1 = font.render(f'{player_1_score}', True, 'blue')
    score_2 = font.render(f'{player_2_score}', True, 'red')


    if game_active:
         screen.fill((98, 98, 98))
         screen.blit(player_1, player_1_rect)
         screen.blit(player_2, player_2_rect)
         screen.blit(ball, ball_rect)
         screen.blit(score_1, (540, 150))
         screen.blit(score_2, (605, 150))
         pygame.draw.line(screen, "white", (screen_width / 2, 0) , (screen_width / 2, screen_height))
         if player_1_score == 3:
             game_active = False
             screen.blit(player_1_win, (370, 240))
             screen.blit(restart_1, (410, 350))
         if player_2_score == 3:
             game_active = False
             screen.blit(player_2_win, (370, 240))
             screen.blit(restart_2, (410, 350))

    pygame.display.flip()
    clock.tick(60)