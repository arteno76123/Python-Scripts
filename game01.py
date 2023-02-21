import pygame
import time

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# the game_goes_on variable will keep the game loop running as long as it is True
game_goes_on = True

x = 200
dx = 1

y = 200
dy = 1

while game_goes_on:

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            game_goes_on = False


    # CURRENT STATE UPDATE
    if x + 60 >= WIDTH or x <= 0:
        dx = -dx
    
    if y + 60 >= HEIGHT or y <= 0:
        dy = -dy    
   
    x += dx   # rate of change for x - "speed"
    y += dy

    # RENDERING
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255,0,0), (x,y, 60, 30))
    pygame.display.update()


pygame.quit()