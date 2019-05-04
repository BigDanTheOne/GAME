from enum import Enum
import consts
import pygame
import random
from pygame import *
from consts import *
from sympy import *
from sympy.geometry import *

pygame.init()
pygame.font.init()


class Cell:
    def __init__(self, cell_width_lower: int, cell_width_upper: int, cell_x: int, cell_y: int,
                 target_lower: (int, int), target_upper: (int, int)):
        """ polygon in tuple are ordered like this:
                 0 |  1
                -------
                 3 |  2
        """
        self.polygon: Polygon
        self.highlighted: bool = False
        self.cell_width_lower = cell_width_lower
        self.cell_width_upper = cell_width_upper
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.polygon = Polygon((target_lower[0], screen_height - target_lower[1]),
                               (target_lower[0] + cell_width_lower, screen_height - target_lower[1]),
                               (target_upper[0] + cell_width_upper, screen_height - target_upper[1]),
                               (target_upper[0], screen_height - target_upper[1]))
        # self.polygon[3] = (target_upper[0], screen_height - target_upper[1])
        # self.polygon[2] = (target_upper[0] + cell_width_upper, screen_height - target_upper[1])
        # self.polygon[1] = (target_lower[0] + cell_width_lower, screen_height - target_lower[1])
        # self.polygon[0] = (target_lower[0], screen_height - target_lower[1])

    def intersection(self, x: int, y: int):
        return self.polygon.encloses_point(Point(x, y))

    def give_coordinates(self):
        return [[self.polygon.vertices[0][0], self.polygon.vertices[0][1]],
                [self.polygon.vertices[1][0], self.polygon.vertices[1][1]],
                [self.polygon.vertices[2][0], self.polygon.vertices[2][1]],
                [self.polygon.vertices[3][0], self.polygon.vertices[3][1]]]


class Map:
    map_matrix: list(list()) = []

    def __init__(self):
        for i in range(N_y):
            zero_target_i = (battlefield_zero_point[0] + (i * battlefield_width * cell_height) / (2 * H),
                             screen_height - battlefield_zero_point[1] + i * cell_height)
            zero_target_i_plus_1 = (battlefield_zero_point[0] + ((i + 1) * battlefield_width * cell_height) / (2 * H),
                                    screen_height - battlefield_zero_point[1] + (i + 1) * cell_height)
            cell_width_lower = battlefield_width * (H - i * cell_height) / (H * N_x)
            cell_width_upper = battlefield_width * (H - (i + 1) * cell_height) / (H * N_x)
            tmp = []
            for j in range(N_x):
                g = Cell(cell_width_lower, cell_width_upper, j, i,
                         (zero_target_i[0] + j * cell_width_lower, zero_target_i[1]),
                         (zero_target_i_plus_1[0] + j * cell_width_upper, zero_target_i_plus_1[1]))
                tmp.append(g)
            self.map_matrix.append(tmp)

    def select_cell(self, cell_x: int, cell_y: int):
        self.map_matrix[cell_x][cell_y].selected = True

    def get_cell_by_x_y(self, x: int, y: int):
        for i in range(len(self.map_matrix)):
            for j in range(len(self.map_matrix[i])):
                if self.map_matrix[i][j].intersection(x, y):
                    print(i, j)
                    return i, j
        return -1, -1