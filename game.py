# imports necessary modules
import sys
import pygame
import time
# initializes pygame
pygame.init()
# sets the width and height of the screen
width, height = 400, 600
screen = pygame.display.set_mode( (width, height) )
# sets the frames per second to 60
FPS = 60
# defines the pygame clock as a shorter variable
clock = pygame.time.Clock()
# creates a font
font = pygame.font.SysFont('Calibri', 25, True, False)
# defines the color white with RGB
WHITE = (255, 255, 255)
# the initial score of zeus
score1 = 0
# the initial score of poseidon
score2 = 0
# initializes the mixer module
pygame.mixer.init()
# imports whistle sound
whistle = pygame.mixer.Sound("aud/Whistle.wav")
# imports a Zeus line from God of War 3
zeus_line = pygame.mixer.Sound("aud/Zeus.wav")
# imports a Poseidon line from God of War 3
poseidon_line = pygame.mixer.Sound("aud/Poseidon.wav")
# imports soccer field image and resizes it
soccer_field = pygame.image.load("img/soccer_field.png")
soccer_field = pygame.transform.scale(soccer_field, (400,600))
# imports soccer ball image and resizes it
soccer_ball = pygame.image.load("img/soccer_ball.png").convert_alpha()
soccer_ball = pygame.transform.scale(soccer_ball, (40,40))
# sets the intial position of the ball
ball_pos = [width/2 - 20, height/2 - 20]
# sets the initial speed of the ball
speed = [0,0]
# imports image of zeus' face and resizes it
zeus = pygame.image.load("img/zeus_face.png").convert_alpha()
zeus = pygame.transform.scale(zeus, (100,100))
# sets the initial position of zeus
zeus_pos = [width/2 - 50, height*3/4 - 50]
# sets the speed of zeus' movement
zeus_vel = [2.5,2.5]
# imports image of poseidon's face and resizes it
poseidon = pygame.image.load("img/poseidon_face.png").convert_alpha()
poseidon = pygame.transform.scale(poseidon, (100,100))
# sets the initial position of poseidon
poseidon_pos = [width/2 - 50, height/4 - 50]
# sets the speed of poseidon's movement
poseidon_vel = [2.5,2.5]
# imports an image of zeus' name
zeus_win = pygame.image.load("img/zeus_win.png").convert_alpha()
# imports and resizes an image of poseidon's name
poseidon_win = pygame.image.load("img/poseidon_win.png").convert_alpha()
poseidon_win = pygame.transform.scale(poseidon_win, (225,94))
# imports and resizes an image of a trophy
wins_logo = pygame.image.load("img/wins_logo.png").convert_alpha()
wins_logo = pygame.transform.scale(wins_logo, (300, 225))
# allows the players to hold down keys and keep registering inputs
pygame.key.set_repeat(10)
# continuous loop
while True:
    # defines the coordinates of the rectangle around the ball 
    ball_left = ball_pos[0] + 3
    ball_right = ball_pos[0] + 37
    ball_top = ball_pos[1] + 3
    ball_bottom = ball_pos[1] + 37
    # defines the coordinates of the rectangle around zeus
    zeus_left = zeus_pos[0] + 3.5
    zeus_right = zeus_pos[0] + 96.5
    zeus_top = zeus_pos[1] + 29
    zeus_bottom = zeus_pos[1] + 81
    # defines the coordinates of the rectangle around poseidon
    poseidon_left = poseidon_pos[0] + 11
    poseidon_right = poseidon_pos[0] + 89
    poseidon_top = poseidon_pos[1] + 11
    poseidon_bottom = poseidon_pos[1] + 81
    # for multiple events pygame registers
    for event in pygame.event.get():
        # if the player quits, the code stops running
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if a key is pressed down
        elif event.type == pygame.KEYDOWN: 
            # if it is the up arrow key
            if event.key == pygame.K_UP:
                # zeus goes up once
                zeus_pos[1] -= zeus_vel[1]
            # if it is the down arrow key
            if event.key == pygame.K_DOWN:
                # zeus goes down once
                zeus_pos[1] += zeus_vel[1]
            # if it is the w key
            if event.key == pygame.K_w:
                # poseidon goes up once
                poseidon_pos[1] -= poseidon_vel[1]
            # if it is the s key
            if event.key == pygame.K_s:
                # poseidon goes down once
                poseidon_pos[1] += poseidon_vel[1]
            # if it is the left arrow key
            if event.key == pygame.K_LEFT:
                # zeus goes to the left once
                zeus_pos[0] -= zeus_vel[0]
            # if it is the right arrow key
            if event.key == pygame.K_RIGHT:
                # zeus goes to the right once
                zeus_pos[0] += zeus_vel[0]
            # if it is the a key
            if event.key == pygame.K_a:
                # poseidon goes to the left once
                poseidon_pos[0] -= poseidon_vel[0]
            # if it is the d key
            if event.key == pygame.K_d:
                # poseidon goes to the right once
                poseidon_pos[0] += poseidon_vel[0]
            # if it is the spacebar
            if event.key == pygame.K_SPACE:
                # it prints poseidon's taunt
                print("Seize the seas!")
        # if the mouse is clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # it prints zeus' taunt
            print("Lightning bolt!")
    # for the y values that the ball occupies
    for x in range(int(ball_top), int(ball_bottom)):
        # for the y values that zeus occupies
        for y in range(int(zeus_top), int(zeus_bottom)):
            # if they share a common y value
            if x == y:
                # if the right of the ball touches the left of zeus
                if int(ball_right) in range(int(zeus_left) - 3, int(zeus_left) + 3):
                    # the ball goes to the left
                    speed[0] = -5
                # if the left of the ball touches the right of zeus
                if int(ball_left) in range(int(zeus_right) - 3, int(zeus_right) + 3):
                    # the ball goes to the right
                    speed[0] = 5
        # for the y values that poseidon occupies
        for z in range(int(poseidon_top), int(poseidon_bottom)):
            # if the ball and poseidon share a common y value
            if x == z:
                # if the right of the ball touches the left of poseidon
                if int(ball_right) in range(int(poseidon_left) - 3, int(poseidon_left) + 3):
                    # the ball goes to the left
                    speed[0] = -5
                # if the left of the ball touches the right of poseidon
                if int(ball_left) in range(int(poseidon_right) - 3, int(poseidon_right) + 3):
                    # the ball goes to the right
                    speed[0] = 5
    # for the x values that the ball occupies
    for a in range(int(ball_left), int(ball_right)):
        # for the x values that zeus occupies
        for b in range(int(zeus_left), int(zeus_right)):
            # if they share a common x value
            if a == b:
                # if the bottom of the ball touches the top of zeus
                if int(ball_bottom) in range(int(zeus_top) - 3, int(zeus_top) + 3):
                    # the ball goes up
                    speed[1] = -5
                # if the top of the ball touches the bottom of zeus
                if int(ball_top) in range(int(zeus_bottom) - 3, int(zeus_bottom) + 3):
                    # the ball goes down
                    speed[1] = 5
        # for the x values that poseidon occupies
        for c in range(int(poseidon_left), int(poseidon_right)):
            # if the ball and poseidon share a common x value
            if a == c:
                # if the bottom of the ball touches the top of poseidon
                if int(ball_bottom) in range(int(poseidon_top) - 3, int(poseidon_top) + 3):
                    # the ball goes up
                    speed[1] = -5
                # if the top of the ball touches the bottom of poseidon
                if int(ball_top) in range(int(poseidon_bottom) - 3, int(poseidon_bottom) + 3):
                    # the ball goes down
                    speed[1] = 5
    # if the ball hits the left or right of the screen
    if ball_left <= 0 or ball_right >= 400:
        # it goes the opposite way
        speed[0] *= -1
    # if the ball hits the top or bottom of the screen
    if ball_top <= 0 or ball_bottom >= 600:
        # it goes in the opposite direction
        speed[1] *= -1
    # if the ball is in between the goal posts
    if ball_left >= 133 and ball_right <= 267:
        # if the ball is touching the top of the screen
        if ball_top <= 0:
            # zeus scores
            score1 += 1
            # the ball goes back to its initial position at rest
            ball_pos = [width/2 - 20, height/2 - 20]
            speed = [0,0]
            # plays the whistle sound and pauses game for 2 seconds
            whistle.play()
        # if the ball touches the bottom of the screen
        if ball_bottom >= 600:
            # poseidon scores
            score2 += 1
            # the ball goes back to its initial position at rest
            ball_pos = [width/2 - 20, height/2 - 20]
            speed = [0,0]
            # plays the whistle sound and pauses game for 2 seconds
            whistle.play()
    # for the ball, the speed is added to the position for each frame in order to get the new position
    ball_pos[0] += speed[0]
    ball_pos[1] += speed[1]
    # the soccer field (background), zeus, poseidon, and the soccer ball are all loaded onto their respective positions
    screen.blit(soccer_field, (0,0))
    screen.blit(zeus, zeus_pos)
    screen.blit(poseidon, poseidon_pos)
    screen.blit(soccer_ball, ball_pos)
    # if zeus reaches a score of 10
    if score1 == 10:
        # the game congratulates zeus with images
        screen.blit(zeus_win, [87.5,225])
        screen.blit(wins_logo, [50,300])
        pygame.display.update()
        # a cool Zeus line that was imported before is played
        zeus_line.play()
        time.sleep(10)
        # the game is closed
        sys.exit()
    # if poseidon reaches a score of 10
    if score2 == 10:
        # the game congratulates poseidon with images, projects a cool line, and ends the game
        screen.blit(poseidon_win, [87.5,175])
        screen.blit(wins_logo, [50,300])
        pygame.display.update()
        # a cool Poseidon line that was imported before is played
        poseidon_line.play()
        time.sleep(10)
        # the game is closed
        sys.exit()
    # the font from before is used to make white text for zeus' score
    text = font.render(str(score1), True, WHITE)
    # the text is loaded onto a position on the screen (in between the upper goal posts)
    screen.blit(text, [195, 571])
    # the font from before is used to make white text for poseidon's score
    text = font.render(str(score2), True, WHITE)
    # the text is loaded onto a position on the screen (in between the lower goal posts)
    screen.blit(text, [195, 8])
    # the screen is refreshed at a rate of 60 frames per second
    pygame.display.update()
    clock.tick(FPS)