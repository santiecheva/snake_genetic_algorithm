import sys
import pygame as pg

from snake.food import Food


pg.init()

class Game:
    def __init__(self, width, height):
        self.screen = pg.display.set_mode((width, height))

        self.initialize_resources()

    def initialize_resources(self):
        self.food = Food()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT: sys.exit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.food.image, (0, 0))
            pg.display.flip()
