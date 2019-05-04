
from grafic_config import *
# Импорт библиотеки pygame
import pygame

# Инициализируем движок pygame
pygame.init()

# Определяем несколько цветов, которые мы будем
# использовать (RGB)
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

pi = 3.141592653


def draw_menu(screen, unit, point, type):
    if type == 'student':
        if unit.sex == 'man':
            color = red
            fon = pygame.image.load(unit_man_foto)
        else:
            color = blue
            fon = pygame.image.load(unit_girl_foto)
        fon = pygame.transform.scale(fon, (menu_x, menu_y))
    else:
        color = green
        fon = pygame.image.load(teacher_foto)
        fon = pygame.transform.scale(fon, (menu_x, menu_y))
        if unit.face != None:
            face = pygame.image.load(unit.face)
            face = pygame.transform.scale(face, (face_x, face_y))
            fon.blit(face, [menu_x / 2 + (menu_x / 2 - face_x) / 2, menu_y / 2 - face_x / 2])

    point1 = [0, (menu_y - shrift_size * len(unit.stats)) / 2]

    for x in unit.stats:
        f2 = pygame.font.SysFont('serif', shrift_size)
        fon.blit(f2.render(x + " : " + str(unit.stats[x]), 1, color), point1)
        point1[1] += shrift_size
    screen.blit(fon, point)


