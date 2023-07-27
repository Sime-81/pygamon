import pygame
import pytmx
import pyscroll

from Player import Player
from map import MapManager


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon - Aventure")

        # Générer un joueur
        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] or pressed[pygame.K_z]:
            self.player.move_up()
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self.player.move_down()
        if pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
            self.player.move_left()
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self.player.move_right()

    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
