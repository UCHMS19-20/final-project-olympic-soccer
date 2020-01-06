import sys
import pygame

pygame.init()

width, height = 400, 600
screen = pygame.display.set_mode( (width, height) )

soccer_field = pygame.image.load("img/soccer_field.png")
soccer_field = pygame.transform.scale(soccer_field, (400,600))
screen.blit(soccer_field, (0,0))
pygame.display.flip()
#update

soccer_ball = pygame.image.load("img/soccer_ball.png")
soccer_ball = pygame.transform.scale(soccer_ball, (50,50))
screen.blit(soccer_ball, (width/2,height/2))
pygame.display.flip()

zeus = pygame.image.load("img/zeus_face.png")
zeus = pygame.transform.scale(zeus, (100,100))
screen.blit(zeus, (width/2,height/4))
pygame.display.flip()

poseidon = pygame.image.load("img/poseidon_face.png")
poseidon = pygame.transform.scale(poseidon, (100,100))
screen.blit(poseidon, (width/2,height/4))
pygame.display.flip()
while True:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evt.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos() # Where is the mouse at?
            zx = mouse_position[0] # mouse_position is in the form [x,y], we only want the x part
            zy = mouse_position[1]
            screen.blit(soccer_field, (0,0))
            screen.blit(soccer_ball, (width/2,height/2))
            screen.blit(zeus, [zx, zy])
            screen.blit(poseidon, (width/2,height/4))
            pygame.display.flip()
        elif evt.type == pygame.MOUSEBUTTONDOWN:
            print("Lightning bolt!")