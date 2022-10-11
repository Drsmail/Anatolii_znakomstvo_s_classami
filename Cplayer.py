import pygame
from Consts import WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def __init__(self, x,y):
        super().__init__()
        self.dx = 0
        self.dy = 0
        self.image = pygame.image.load("картинка")
        self.image.fill(pygame.Color("green"))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def SayHello(self):
        print("Hello i am Player")

    def Move(self):
        self.dx, self.dy = 0, 0
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
                self.dx, self.dy = 0, -1
        elif key[pygame.K_s]:
                self.dx, self.dy = 0, 1
        elif key[pygame.K_a]:
                self.dx, self.dy = -1, 0
        elif key[pygame.K_d]:
                self.dx, self.dy = 1, 0

        self.rect.center = (self.rect.centerx + (self.dx * 2), self.rect.centery + (self.dy * 2))


# main