import sys
import pygame

pygame.init()

width, height = 400, 600
screen = pygame.display.set_mode( (width, height) )

soccer_field = pygame.image.load("img/soccer_field.png")
soccer_field = pygame.transform.scale(soccer_field, (400,600))

soccer_ball = pygame.image.load("img/soccer_ball.png").convert_alpha()
soccer_ball = pygame.transform.scale(soccer_ball, (50,50))

zeus = pygame.image.load("img/zeus_face.png").convert_alpha()
zeus = pygame.transform.scale(zeus, (100,100))

poseidon = pygame.image.load("img/poseidon_face.png").convert_alpha()
poseidon = pygame.transform.scale(poseidon, (100,100))

while True:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evt.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos() # Where is the mouse at?
            zeus_rect = zeus.get_rect()
            zeus_rect.center = mouse_position
            screen.blit(soccer_field, (0,0))
            screen.blit(soccer_ball, (width/2,height/2))
            screen.blit(zeus, zeus_rect)
            pygame.mouse.set_visible(False)
            screen.blit(poseidon, (width/2,height/4))
            pygame.display.flip()
        elif evt.type == pygame.MOUSEBUTTONDOWN:
            print("Lightning bolt!")