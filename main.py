import pygame
from Cplayer import Player

RES = 800
fps = 60



screen = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

player = Player(700,800)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    player.Move()
    screen.fill('black')
    player.draw(screen)
    pygame.display.update()
    clock.tick(fps)


