from enum import Enum
import consts
import pygame
import random
from pygame import *
from consts import *
from images import *
from renderer import *
from examenator import *
from students import *

pygame.init()
pygame.font.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_widt, screen_height))
        self.run = True
        self.screen.blit(background, (0, 0))
        self.renderer = Renderer(self.screen)

    def play(self):
        map = Map()
        while self.run:
            pygame.time.delay(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()

            self.renderer.render_background()
            self.renderer.render_map(map)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.play()
