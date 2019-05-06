import pygame
from pygame import *
from consts import *
pygame.init()
pygame.font.init()

#TODO: Somehow add .convert()
background = pygame.image.load('Images/background.jpg')
background = pygame.transform.scale(background, (screen_widt, screen_height))
student_body = pygame.image.load('Images/Hero.png')
student_head = pygame.image.load('Images/Hero.png')
