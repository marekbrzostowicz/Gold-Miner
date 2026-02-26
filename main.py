from fireflies import Fireflies

import pygame
import math
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

tick_radius = 90

site = True

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('pygame_window')
clock = pygame.time.Clock()



fireflies = Fireflies()




def draw_hak(tick ): 
        start_pos = (300, 300)
        length = 200
       
        radius = 0.5 - tick
     
        radius_ = math.radians(radius)

        end_x = start_pos[0] - length * math.sin(radius_)
        end_y = start_pos[1] + length * math.cos(radius_)

        pygame.draw.line(window, (255,0,0), (300,300), (300,500))
        pygame.draw.line(window, (255,0,0), start_pos, (end_x, end_y))

run = True

while run:

    

    clock.tick(60)
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            run = False
    window.fill((0,0,0))

    pygame.draw.line(window, (255, 255, 0), (0, 100), (1200, 100))

    #--------------------fireflies
    fireflies.spawn_fireflies()
    fireflies.draw_fireflies(window)
    fireflies.update_fireflie_position()

    if tick_radius <= -90:
         site = False
    if tick_radius >= 90:
         site = True
    if site == True:
        tick_radius = tick_radius - 0.5
    else:
         tick_radius = tick_radius + 0.5

    draw_hak(tick_radius)

    pygame.display.update()

pygame.quit()