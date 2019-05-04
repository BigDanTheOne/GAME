from strategy import *
from menu_stats import *
from consts import *
import pygame


class BBox:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = bbox_r

    def intersect(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** (0.5) <= self.r


class Unit:
    # imgHeadad':  pygame.Surface
    # imgBody:  pygame.Surface
    # bbox: BBox(100, 100, 10)
    # speed: int = unitSpeed

    # def __init__(self, imgHead, imgBody):
    #     self.imgHead = pygame.image.load(imgHead)
    #     self.imgBody = pygame.image.load(imgBody)
    def __init__(self, point=[0, 0]):
        self.bbox = BBox(point[0], point[1])

    def step(self, target, delta_t):
        new_bbox = copy.deepcopy(self.bbox)
        new_bbox.x += self.speed * math.sin(
            math.atan2(self.target[0] - self.bbox.x,
                       self.target[1] - self.bbox.y)) * delta_t
        new_bbox.y += self.speed * math.cos(
            math.atan2(self.target[0] - self.bbox.x,
                       self.target[1] - self.bbox.y)) * delta_t
        self.bbox = new_bbox

    hit = hit1

    def move(self, target, delta_t):
        pass

    def death(self):
        pass

    def draw_menu(self, screen):
        x, y = pygame.mouse.get_pos()
        if self.bbox.intersect(x, y) and pygame.mouse.get_pressed()[2]:
            draw_menu(screen, self, [screen_widt - menu_x, 0], self.type)
