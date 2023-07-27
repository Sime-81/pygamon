import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load('../sprites/Player.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.current = 0
        self.anime_num = 0
        self.animations = {
            'down1': self.get_image(0, 0),
            'down2': self.get_image(32, 0),
            'down3': self.get_image(64, 0),
            'left1': self.get_image(0, 32),
            'left2': self.get_image(32, 32),
            'left3': self.get_image(64, 32),
            'right1': self.get_image(0, 64),
            'right2': self.get_image(32, 64),
            'right3': self.get_image(64, 64),
            'up1': self.get_image(0, 96),
            'up2': self.get_image(32, 96),
            'up3': self.get_image(64, 96),
        }

    def animate(self, direction):

        self.current += 1

        if 1 <= self.current <= 9:
            self.anime_num = 1
        elif 10 <= self.current <= 18:
            self.anime_num = 3
        else:
            self.current = 1

        self.image = self.animations[direction + str(self.anime_num)]
        self.image.set_colorkey([0, 0, 0])

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
