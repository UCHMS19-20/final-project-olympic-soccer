import sys
import pygame

pygame.init()

width, height = 400, 600
screen = pygame.display.set_mode( (width, height) )
FPS = 60
clock = pygame.time.Clock()
black = (0,0,0)

soccer_field = pygame.image.load("img/soccer_field.png")
soccer_field = pygame.transform.scale(soccer_field, (400,600))

soccer_ball = pygame.image.load("img/soccer_ball.png").convert_alpha()
soccer_ball = pygame.transform.scale(soccer_ball, (40,40))
ball_pos = [width/2, height/2]
speed = [0,0]

zeus = pygame.image.load("img/zeus_face.png").convert_alpha()
zeus = pygame.transform.scale(zeus, (100,100))
zeus_pos = [width/2, height*3/4]
zeus_vel = [2.5,2.5]

poseidon = pygame.image.load("img/poseidon_face.png").convert_alpha()
poseidon = pygame.transform.scale(poseidon, (100,100))
poseidon_pos = [width/2, height/4]
poseidon_vel = [2.5,2.5]

pygame.key.set_repeat(10)

while True:
    
    ball_left = ball_pos[0]
    ball_right = ball_pos[0] + 40
    ball_top = ball_pos[1]
    ball_bottom = ball_pos[1] + 40

    zeus_left = zeus_pos[0]
    zeus_right = zeus_pos[0] + 100
    zeus_top = zeus_pos[1]
    zeus_bottom = zeus_pos[1] + 100

    poseidon_left = zeus_pos[0]
    poseidon_right = zeus_pos[0] + 100
    poseidon_top = zeus_pos[1]
    poseidon_bottom = zeus_pos[1] + 100
  
    if zeus_left <= ball_left <= zeus_right or zeus_left <= ball_right <= zeus_right:
        if zeus_top <= ball_bottom <= zeus_top + 40:
            speed[1] = -5
        if zeus_bottom - 40 <= ball_top <= zeus_bottom:
            speed[1] = 5
    if zeus_top <= ball_top <= zeus_bottom or zeus_top <= ball_bottom <= zeus_bottom:
        if zeus_left <= ball_right <= zeus_left + 40:
            speed[0] = -5
        if zeus_right - 40 <= ball_left <= zeus_right:
            speed[0] = 5
    
    if poseidon_left <= ball_left <= poseidon_right or poseidon_left <= ball_right <= poseidon_right:
        if poseidon_top <= ball_bottom <= poseidon_top + 40:
            speed[1] = -5
        if poseidon_bottom - 40 <= ball_top <= poseidon_bottom:
            speed[1] = 5
    if poseidon_top <= ball_top <= poseidon_bottom or poseidon_top <= ball_bottom <= poseidon_bottom:
        if poseidon_left <= ball_right <= poseidon_left + 40:
            speed[0] = -5
        if poseidon_right - 40 <= ball_left <= poseidon_right:
            speed[0] = 5

    if ball_left <= 0 or ball_right >= 400:
        speed[0] *= -1
    if ball_top <= 0 or ball_bottom >= 600:
        speed[1] *= -1

    ball_left += speed[0]
    ball_top += speed[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                zeus_top -= zeus_vel[1]
            if event.key == pygame.K_DOWN:
                zeus_top += zeus_vel[1]
            if event.key == pygame.K_w:
                poseidon_top -= poseidon_vel[1]
            if event.key == pygame.K_s:
                poseidon_top += poseidon_vel[1]

            if event.key == pygame.K_LEFT:
                zeus_left -= zeus_vel[0]
            if event.key == pygame.K_RIGHT:
                zeus_left += zeus_vel[0]
            if event.key == pygame.K_a:
                poseidon_left -= poseidon_vel[0]
            if event.key == pygame.K_d:
                poseidon_left += poseidon_vel[0]
            
            if event.key == pygame.K_SPACE:
                print("Seize the seas!")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Lightning bolt!")

    screen.blit(soccer_field, (0,0))
    screen.blit(zeus, zeus_pos)
    screen.blit(poseidon, poseidon_pos)
    screen.blit(soccer_ball, ball_pos)
    
    pygame.display.update()
    clock.tick(FPS)