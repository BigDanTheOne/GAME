import pygame
from grafic_config import *
from pygame import *
from consts import *

pygame.init()
pygame.font.init()

background = pygame.image.load('Images/background.jpg')
background = pygame.transform.scale(background, (screen_widt, screen_height))
head = dict()
body = dict()
body['student'] = pygame.image.load('Images/Hero.png')
head['student'] = pygame.image.load('Images/Hero.png')
head['lecturer'] = pygame.image.load('Images/examinator.png')
body['lecturer'] = pygame.image.load('Images/examinator.png')
head['seminarist'] = pygame.image.load('Images/examinator.png')
body['seminarist'] = pygame.image.load('Images/examinator.png')
fon1 = {'student': {'man': pygame.image.load(student_man_foto), 'woman': pygame.image.load(student_girl_foto)},
       'lecturer': pygame.image.load(teacher_foto), 'seminarist' : pygame.image.load(teacher_foto)}
