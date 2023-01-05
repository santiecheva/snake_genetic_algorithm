import pygame as pg
import os


def load_images(path):
    image = pg.image.load(path)
    return image.convert()

