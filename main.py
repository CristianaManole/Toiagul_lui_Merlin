import os
import random
import math
import pygame
from os import listdir

#cu ajutorul acestei bibloteci facem split la imaginile din folderul assets
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Toiagul lui Merlin")

WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_VEL = 5

winodws = pygame.display.set_mode((WIDTH, HEIGHT))




class Player(pygame.sprite.Sprite):
    #clasa Player mosteneste clasa Sprite pentru a face o coliziune perfecta intre Sprite-uri
    COLOR = (255, 0, 0)
    GRAVITY = 1
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)



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


def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)
        # tile reprezinta pozitia
    player.draw(window)
    pygame.display.update()

def handle_movement(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    #am pus valoarea 0 pentru ca daca nu apasam nimic, player-ul sa nu se miste

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)

def main(window):
    clock = pygame.time.Clock()
    # setez background-ul
    background, bg_image = get_background("Dark_blue.png")

    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        player.loop(FPS)
        handle_movement(player)
        draw(window, background, bg_image, player)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(winodws)



