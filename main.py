import os
import random
import math
import pygame
from os import listdir

#cu ajutorul acestei bibloteci facem split la imaginile din folderul assets
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Toiagul lui Merlin")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

winodws = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    # x, y, width, height, dar pe mine nu ma intereseaza x si y
    tiles = []
    #tiles este o lista de pozitii

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            # ma pozitioneaza in coltul din stanga sus, pos primeste coordonatele
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)
        # tile reprezinta pozitia

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    # setez background-ul
    background, bg_image = get_background("Brown.png")

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window, background, bg_image)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(winodws)



