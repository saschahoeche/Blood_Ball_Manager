# main file
import pygame
import sys

# constants go here
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

pygame.init()

# create window
gameWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blood Ball Manager")


### GAME LOOP START ###
gameRunning = True

while gameRunning:
    
    ### EVENT LOOP ###
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            gameRunning = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("UP")            
            if event.key == pygame.K_a:
                print("LEFT")            
            if event.key == pygame.K_s:
                print("DOWN")            
            if event.key == pygame.K_d:
                print("RIGHT")
            
    ### GAME CONTENT ###
    gameWindow.fill((255, 255, 255))
    
    pygame.display.update()
    

# close all modules and return memory
pygame.quit()
sys.exit()