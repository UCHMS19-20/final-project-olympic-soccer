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

    ball_left = ball_pos[0]
    ball_right = ball_pos[0] + 40
    ball_top = ball_pos[1]
    ball_bottom = ball_pos[1] + 40

    zeus_left = zeus_pos[0]
    zeus_right = zeus_pos[0] + 100
    zeus_top = zeus_pos[1]
    zeus_bottom = zeus_pos[1] + 100

    poseidon_left = poseidon_pos[0]
    poseidon_right = poseidon_pos[0] + 100
    poseidon_top = poseidon_pos[1]
    poseidon_bottom = poseidon_pos[1] + 100

    for x in range(ball_left, ball_right):
        for y in range(zeus_left, zeus_right):
            if x == y:
                if zeus_top in range(ball_bottom - 3, ball_bottom + 3):
                    speed[1] = -5
                if zeus_bottom in range(ball_top - 3, ball_top + 3):
                    speed[1] = 5
        for z in range(poseidon_left, poseidon_right):
            if x == z:
                if poseidon_top in range(ball_bottom - 3, ball_bottom + 3):
                    speed[1] = -5
                if zeus_bottom in range(ball_top - 3, ball_top + 3):
                    speed[1] = 5

    for u in range(ball_top, ball_bottom):
        for v in range(zeus_top, zeus_bottom):
            if u == v:
                if zeus_left in range(ball_right - 3, ball_right + 3):
                    speed[0] = -5
                if zeus_right in range(ball_left - 3, ball_left + 3):
                    speed[0] = 5
        for t in range(poseidon_top, poseidon_bottom):
            if u == t:
                if poseidon_left in range(ball_right - 3, ball_right + 3):
                    speed[0] = -5
                if poseidon_right in range(ball_left - 3, ball_left + 3):
                    speed[0] = 5
    
    if ball_top == 0 or ball_bottom == 600:
        if ball_left >= 267 and ball_right <= 358:
            ball_pos = [width/2, height/2]
            speed = [0,0]

    if ball_left <= 0 or ball_right >= 400:
        speed[0] *= -1
    if ball_top <= 0 or ball_bottom >= 600:
        speed[1] *= -1

    ball_pos[0] += speed[0]
    ball_pos[1] += speed[1]

    screen.blit(soccer_field, (0,0))
    screen.blit(zeus, zeus_pos)
    screen.blit(poseidon, poseidon_pos)
    screen.blit(soccer_ball, ball_pos)
    
    pygame.display.update()
    clock.tick(FPS)