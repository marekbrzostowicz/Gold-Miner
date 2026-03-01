from fireflies import Fireflies
from water import Water

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

TLO = pygame.image.load('./images/Screenshot 2026-03-01 233232.png').convert_alpha()
TLO_ = pygame.transform.scale(TLO, (SCREEN_WIDTH, 100))

fireflies = Fireflies()
water = Water()

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

    window.blit(TLO_, (0, 0))

    #--------------------fireflies
    # fireflies.update_x()
    fireflies.spawn_fireflies()
    fireflies.update_fireflie_position()
    fireflies.draw_fireflies(window)

    #-------------------water
    water.spawn_water()
    water.draw_water(window)
    water.update_water_position()
    

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