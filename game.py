import sys
import pygame

pygame.init()

width, height = 626, 915
screen = pygame.display.set_mode( (width, height) )

for evt in pygame.event.get():
    if evt.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

background_image = pygame.image.load("img/soccer_field.png")
screen.blit(background_image, (0,0))
pygame.display.flip()