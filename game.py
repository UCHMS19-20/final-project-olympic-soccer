import sys
import pygame

pygame.init()

width, height = 400, 600
screen = pygame.display.set_mode( (width, height) )
FPS = 60
clock = pygame.time.Clock()

soccer_field = pygame.image.load("img/soccer_field.png")
soccer_field = pygame.transform.scale(soccer_field, (400,600))
soccer_field_rect = soccer_field.get_rect()

soccer_ball = pygame.image.load("img/soccer_ball.png").convert_alpha()
soccer_ball = pygame.transform.scale(soccer_ball, (40,40))
ball_rect = soccer_ball.get_rect()
ball_rect_pos = [width/2, height/2]
speed = [0,0]

zeus = pygame.image.load("img/zeus_face.png").convert_alpha()
zeus = pygame.transform.scale(zeus, (100,100))
zeus_rect = zeus.get_rect()
zeus_rect_pos = [width/2, height*3/4]
zeus_rect_vel = [10,10]

poseidon = pygame.image.load("img/poseidon_face.png").convert_alpha()
poseidon = pygame.transform.scale(poseidon, (100,100))
poseidon_rect = poseidon.get_rect()
poseidon_rect_pos = [width/2, height/4]
poseidon_rect_vel = [10,10]

while True:
    if ball_rect.top == zeus_rect.bottom or ball_rect.top == poseidon_rect.bottom:
        speed[1] = -40
    if ball_rect.bottom == zeus_rect.top or ball_rect.bottom == poseidon_rect.top:
        speed[1] = 40
    if ball_rect.right == zeus_rect.left or ball_rect.right == poseidon_rect.left:
        speed[0] = -40
    if ball_rect.left == zeus_rect.right or ball_rect.left == poseidon_rect.right:
        speed[0] = 40
    
    ball_rect_pos[0] += speed[0]
    ball_rect_pos[1] += speed[1]

# if statement for if the two things are close, the other things are applicable, put margins of error

    if ball_rect.right - 10 < zeus_rect.left < ball_rect.right + 10 or ball_rect.left < zeus_rect.right < ball_rect.left:
        speed[0] -= speed[0]
    if ball_rect.bottom < zeus_rect.top < ball_rect.bottom or ball_rect.top < zeus_rect.bottom < ball_rect.top:
        speed[1] -= speed[1]

    if ball_rect.right < poseidon_rect.left < ball_rect.right or ball_rect.left < poseidon_rect.right < ball_rect.left:
        speed[0] -= speed[0]
    if ball_rect.bottom < poseidon_rect.top < ball_rect.bottom or ball_rect.top < poseidon_rect.bottom < ball_rect.top:
        speed[1] -= speed[1]

    if ball_rect.left or ball_rect.right == soccer_field_rect.left or soccer_field_rect.right:
        speed[0] -= speed[0]
    if ball_rect.top or ball_rect.bottom == soccer_field_rect.top or soccer_field_rect.bottom:
        speed[1] -= speed[1]

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                zeus_rect_pos[1] -= zeus_rect_vel[1]
            if event.key == pygame.K_DOWN:
                zeus_rect_pos[1] += zeus_rect_vel[1]
            if event.key == pygame.K_w:
                poseidon_rect_pos[1] -= poseidon_rect_vel[1]
            if event.key == pygame.K_s:
                poseidon_rect_pos[1] += poseidon_rect_vel[1]

            if event.key == pygame.K_LEFT:
                zeus_rect_pos[0] -= zeus_rect_vel[0]
            if event.key == pygame.K_RIGHT:
                zeus_rect_pos[0] += zeus_rect_vel[0]
            if event.key == pygame.K_a:
                poseidon_rect_pos[0] -= poseidon_rect_vel[0]
            if event.key == pygame.K_d:
                poseidon_rect_pos[0] += poseidon_rect_vel[0]
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Lightning bolt!")

    screen.blit(soccer_field, (0,0))
    screen.blit(zeus, zeus_rect_pos)
    screen.blit(poseidon, poseidon_rect_pos)
    screen.blit(soccer_ball, ball_rect_pos)
    
    pygame.display.update()
    clock.tick(FPS)