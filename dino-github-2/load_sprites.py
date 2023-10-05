import pygame, pathlib, os

def load_image(image: str):
    path = os.path.abspath(__file__ + "/..") + "/sprites/" + image
    return pygame.image.load(path)