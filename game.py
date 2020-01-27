import sys
import pygame

pygame.init()

width, height = 400, 600
screen = pygame.display.set_mode( (width, height) )
FPS = 60
clock = pygame.time.Clock()

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
    if speed[1] == 0:    
        if ball_pos[0] <= zeus_pos[0] <= ball_pos[0] + 40 or ball_pos[0] <= poseidon_pos[0] <= ball_pos[0] + 40:
            if ball_pos[1] <= zeus_pos[1] + 100 <= ball_pos[1] + 40 or ball_pos[1] <= poseidon_pos[1] + 100 <= ball_pos[1] + 40:
                speed[1] = -5
            if ball_pos[1] + 40 >= zeus_pos[1] >= ball_pos[1] or ball_pos[1] + 40 >= poseidon_pos[1] >= ball_pos[1]:
                speed[1] = 5
    if speed[0] == 0:
        if ball_pos[1] <= zeus_pos[1] <= ball_pos[1] + 40 or ball_pos[1] <= poseidon_pos[1] <= ball_pos[1] + 40:   
            if ball_pos[0] + 40 >= zeus_pos[0] >= ball_pos[0] or ball_pos[0] + 40 >= poseidon_pos[0] >= ball_pos[0]:
                speed[0] = -5
            if ball_pos[0] <= zeus_pos[0] + 100 <= ball_pos[0] + 40 or ball_pos[0] <= poseidon_pos[0] + 100 <= ball_pos[0] + 40:
                speed[0] = 5

    if ball_pos[1] <= zeus_pos[1] <= ball_pos[1] + 40:
        if ball_pos[0] <= zeus_pos[0] <= ball_pos[0] + 40:
            speed[0] *= -1
    if ball_pos[0] <= zeus_pos[0] <= ball_pos[0] + 40:
        if ball_pos[1] <= zeus_pos[1] <= ball_pos[1] + 40:
            speed[1] *= -1
    
    if ball_pos[1] <= poseidon_pos[1] <= ball_pos[1] + 40:
        if ball_pos[0] <= poseidon_pos[0] <= ball_pos[0] + 40:
            speed[0] *= -1
    if ball_pos[0] <= poseidon_pos[0] <= ball_pos[0] + 40:
        if ball_pos[1] <= poseidon_pos[1] <= ball_pos[1] + 40:
            speed[1] *= -1

    if ball_pos[0] <= 0 or ball_pos[0] + 40 >= 400:
        speed[0] *= -1
    if ball_pos[1] <= 0 or ball_pos[1] + 40 >= 600:
        speed[1] *= -1

    ball_pos[0] += speed[0]
    ball_pos[1] += speed[1]

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                zeus_pos[1] -= zeus_vel[1]
            if event.key == pygame.K_DOWN:
                zeus_pos[1] += zeus_vel[1]
            if event.key == pygame.K_w:
                poseidon_pos[1] -= poseidon_vel[1]
            if event.key == pygame.K_s:
                poseidon_pos[1] += poseidon_vel[1]

            if event.key == pygame.K_LEFT:
                zeus_pos[0] -= zeus_vel[0]
            if event.key == pygame.K_RIGHT:
                zeus_pos[0] += zeus_vel[0]
            if event.key == pygame.K_a:
                poseidon_pos[0] -= poseidon_vel[0]
            if event.key == pygame.K_d:
                poseidon_pos[0] += poseidon_vel[0]
            
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