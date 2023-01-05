import pygame as pg


def load_images(path):
    image = pg.image.load(path)
    return image.convert()
