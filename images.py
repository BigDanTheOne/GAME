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
body['student'] = pygame.image.load('Images/student.png')
body['student'] = pygame.transform.scale(body['student'], (int(body['student'].get_size()[0]*0.65), int(body['student'].get_size()[1]*0.65)))
head['student'] = pygame.image.load('Images/student.png')
head['lecturer'] = pygame.image.load('Images/examinator.png')
body['player'] = pygame.image.load('Images/player.png')
body['player'] = pygame.transform.scale(body['player'], (int(body['player'].get_size()[0]*0.65), int(body['player'].get_size()[1]*0.65)))
head['player'] = pygame.image.load('Images/player.png')
head['player'] = pygame.image.load('Images/player.png')
body['lecturer'] = pygame.image.load('Images/examinator.png')
body['lecturer'] = pygame.transform.scale(body['lecturer'], (int(body['lecturer'].get_size()[0]*1.5), int(body['lecturer'].get_size()[1]*1.5)))
head['seminarist'] = pygame.image.load('Images/examinator.png')
body['seminarist'] = pygame.image.load('Images/examinator.png')
fon1 = {'student': {'man': pygame.image.load(student_man_foto), 'woman': pygame.image.load(student_girl_foto)},
       'lecturer': pygame.image.load(teacher_foto), 'seminarist' : pygame.image.load(teacher_foto)}
