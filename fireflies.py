import random
import pygame

class Fireflies:
    def __init__(self):
        self.list_of_fireflies = []

    def spawn_fireflies(self):
        random_number = random.randint(0, 30)
        if random_number == 1:
            if len(self.list_of_fireflies) < 5:
                new_firefly = {
                    "position": [500, 500],
                    "counter": random.randint(0, 10)
                }
                self.list_of_fireflies.append(new_firefly)

    def update_fireflie_position(self):
        for firefly in self.list_of_fireflies:
            pass

            


    def draw_fireflies(self, window):
        for firefly in self.list_of_fireflies:
            pygame.draw.rect(window, (255, 0, 255), (firefly["position"], (10, 10)))
