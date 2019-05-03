from students import *
import consts
import pygame
from images import *
from map import *
class Renderer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def render_static_unit(self, u: Unit):
        x = u.x
        y = u.y
        image = u.imgBody
        self.screen.blit(image, (x, y))

    def rotate_img(self, image, angle):
        """rotate a Surface, maintaining position."""

        loc = image.get_rect().center  # rot_image is not defined
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite

    def render_background(self):
        self.screen.blit(background, (0, 0))


    def render_map(self, map: Map):
        x, y = pygame.mouse.get_pos()
        cell_x, cell_y = map.get_cell_by_x_y(x, y)

        for i in range(len(map.map_matrix)):
            for j in range(len(map.map_matrix[i])):
                if not (cell_y == i and cell_x == j):
                    pass
                    #pygame.draw.polygon(self.screen, pygame.Color(0, 0, 0), map.map_matrix[j][i].give_coordinates(), 1)
                else:
                    pygame.draw.polygon(self.screen, pygame.Color(255, 255, 255) ,map.map_matrix[j][i].give_coordinates(), 1)
                    print(i ,j)
