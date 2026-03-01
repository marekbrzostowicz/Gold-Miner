import random
import pygame

class Fireflies:
    def __init__(self):
        self.list_of_fireflies = []
        self.side_of_fireflies = True
        self.spawn_flag = True
        self.random_x = 200
        self.spawn_pos = [self.random_x, 50]
        
    counter = 0

    def random_x_position(self):
        if self.side_of_fireflies:
            self.random_x = random.randint(200, 500)
        else:
            self.random_x = random.randint(700, 1100)

        self.spawn_pos[0] = self.random_x

    def spawn_fireflies(self):
        
        random_number = random.randint(0, 150) 
        if self.spawn_flag == True:
            if random_number == 1:
                        
                new_firefly = {
                    "position": self.spawn_pos.copy(),
                    "counter": random.randint(0, 10),
                    "random_g": random.randint(170, 250)
                }
                self.list_of_fireflies.append(new_firefly)

                if len(self.list_of_fireflies) == 5:
                    self.spawn_flag = not self.spawn_flag

        Fireflies.counter += 1

        if self.spawn_flag == False and Fireflies.counter > 1100:
            if random_number == 1:
                if len(self.list_of_fireflies) != 0:
                    self.list_of_fireflies.pop()
            if len(self.list_of_fireflies) == 0:
                self.spawn_flag = not self.spawn_flag
                self.side_of_fireflies = not self.side_of_fireflies
                Fireflies.counter = 0
                self.random_x_position()


    def draw_glow(self, window, x, y):

        radius = 12
        glow_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        middle = (radius, radius)

        pygame.draw.circle(glow_surface, (255, 200, 0, 30), middle, radius)
        pygame.draw.circle(glow_surface, (255, 255, 0, 90), middle, radius - 5)

        window.blit(glow_surface, (x, y))
        
    def update_fireflie_position(self):
            for firefly in self.list_of_fireflies:
                firefly["counter"] += 1

                if firefly["counter"] > 15:
                    random_x = random.randint(-5, 5)
                    random_y = random.randint(-10, 10)

                    x, y = firefly["position"]

                    min_x = self.spawn_pos[0] - 45
                    max_x = self.spawn_pos[0] + 45
                    min_y = self.spawn_pos[1] - 45
                    max_y = self.spawn_pos[1] + 35

                    if x < min_x:
                        firefly["position"][0] = min_x
                    elif x > max_x: 
                        firefly["position"][0] = max_x
                    
                    if y < min_y:
                        firefly["position"][1] = min_y
                    elif y > max_y:
                        firefly["position"][1] = max_y

                    firefly["position"][0] += random_x
                    firefly["position"][1] += random_y
                    
                    firefly["counter"] = random.randint(0, 5)

    def draw_fireflies(self, window):
        for firefly in self.list_of_fireflies:
            pygame.draw.rect(window, (255, firefly["random_g"], 120), (firefly["position"], (4, 4)))
            self.draw_glow(window, firefly["position"][0] - 10, firefly["position"][1] - 10)
