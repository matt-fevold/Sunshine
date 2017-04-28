#play game
import sys
import random
import math

import pygame


from pygame.locals import *

debugging = True

pygame.init()
screen = pygame.display.set_mode((800, 600))
surface = pygame.Surface((100, 100))
done = False
is_random = True
x = 30
y = 30
red = 0
green = 0 
blue = 0
box_x =25
box_y =25

clock = pygame.time.Clock()

def debug(x):
        if(debugging==True):
                print(x)

def randomInt(t=-1):
        if(t==-1):
                return random.randrange(255)
        else:
                x = (random.choice([-1,-2,0]) + t)%255
                return abs(x)
        
def drawRectangle(var_screen, var_color, X, Y, box_X, box_Y, spacing):
        pygame.draw.rect(var_screen, var_color, pygame.Rect(X + spacing, Y, box_X, box_Y))
 

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_random = not is_random
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
        if is_random:
                color = (red, green, blue)
        else:
                red = randomInt(red)
                green = randomInt(green)
                blue = randomInt(blue)
                color = (red, green, blue)
                
        for t in range(0,4):
                #print("t: ",t," x: ",x," y: ",y," box_x: ",box_x,
                      #" box_y: ",box_y)
                #drawRectangle(screen, color, x, y, box_x, box_y, 20)
                pygame.draw.rect(screen, color, pygame.Rect(x+box_x+(40*t), y, box_x, box_y))
        #pygame.draw.rect(screen, color, pygame.Rect(x+20+box_x, y+20, box_x, box_y))
            
        pygame.display.flip()
        clock.tick(60)



			
			
