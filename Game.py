#play game
import sys
import random

import pygame


from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
surface = pygame.Surface((100, 100))
done = False
is_blue = True
x = 30
y = 30
red = 0
green = 0 
blue = 0
box_x =25
box_y =25

clock = pygame.time.Clock()

def randomInt():
	return random.randrange(255)


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                        red = randomInt()
                        green = randomInt()
                        blue = randomInt()

        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1]:
            done = True
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        else:
            

            if pressed[pygame.K_UP]: y -= 5
            if pressed[pygame.K_DOWN]: y += 5
            if pressed[pygame.K_LEFT]: x -= 5
            if pressed[pygame.K_RIGHT]: x += 5
            if pressed[pygame.K_s]: box_y -= 2
            if pressed[pygame.K_w]: box_y += 2
            if pressed[pygame.K_a]: box_x -=2
            if pressed[pygame.K_d]: box_x +=2
            
            screen.fill((0, 0, 0))
            if is_blue: color = (red, green, blue)
            else: color = (randomInt(), randomInt(), randomInt())
            pygame.draw.rect(screen, color, pygame.Rect(x, y, box_x, box_y))
            
            pygame.display.flip()
            clock.tick(60)



			
			
