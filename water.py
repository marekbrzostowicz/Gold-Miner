import pygame

class Water:
    def __init__(self):
        self.list_of_water_drops = []
        self.splashes = [] 
        self.starting_water_drop_length = 3
        self.x_positions_and_counters = {
            100: 200,
            170: 250,
            900: 170,
        }

    def spawn_water(self):
        if len(self.list_of_water_drops) < 3:
            for key, value in self.x_positions_and_counters.items():
                new_drop = {
                    "position": key,
                    "counter": 0,
                    "y": 0
                }
                self.list_of_water_drops.append(new_drop)

    def draw_water(self, window):
        for i in range(len(self.list_of_water_drops)):
            
            self.list_of_water_drops[i]["counter"] += 1
            if self.list_of_water_drops[i]["counter"] > self.x_positions_and_counters[self.list_of_water_drops[i]["position"]]:
                pygame.draw.rect(window, (90, 120, 153), (self.list_of_water_drops[i]["position"], self.list_of_water_drops[i]["y"], self.starting_water_drop_length, 9))


        for splash in self.splashes:
            rozstaw = splash["timer"] * 1.5 
            wysokosc_odbicia = splash["timer"] * 0.5


            pygame.draw.rect(window, (90, 120, 153), (splash["x"] - rozstaw, splash["y"] - wysokosc_odbicia, 2, 2))
            pygame.draw.rect(window, (90, 120, 153), (splash["x"] + self.starting_water_drop_length + rozstaw, splash["y"] - wysokosc_odbicia, 2, 2))

    def update_water_position(self):

        for drop in self.list_of_water_drops:
            if drop["counter"] > self.x_positions_and_counters[drop["position"]]:
                drop["y"] += 2

            if drop["y"] >= 95:
                nowy_rozprysk = {
                    "x": drop["position"],
                    "y": 95,
                    "timer": 0 
                }
                self.splashes.append(nowy_rozprysk)

                drop["y"] = 0
                drop["counter"] = 0
        
        for splash in self.splashes[:]:
            splash["timer"] += 1
            if splash["timer"] > 10:
                self.splashes.remove(splash)