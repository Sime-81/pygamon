import pygame
from animation import AnimateSprite


class Player(AnimateSprite):

    def __init__(self, x, y):
        super().__init__()
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 1.5

    def save_location(self): self.old_position = self.position.copy()

    def move_right(self):
        self.position[0] += self.speed
        self.animate('right')

    def move_left(self):
        self.position[0] -= self.speed
        self.animate('left')

    def move_up(self):
        self.position[1] -= self.speed
        self.animate('up')

    def move_down(self):
        self.position[1] += self.speed
        self.animate('down')

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom