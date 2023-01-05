import sys
import pygame as pg
from params import load_images



pg.init()

size = width, height = 500, 500
speed = [2, 2]
black = 0, 0, 0

screen = pg.display.set_mode(size)
image = load_images('./assets/apple.png')
while True:
    for event in pg.event.get():

        if event.type == pg.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(image,(0,0))
    pg.display.flip()