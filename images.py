import pygame
from pygame import *
from consts import *
pygame.init()
pygame.font.init()


background = pygame.image.load('Images/background.jpg')
background = pygame.transform.scale(background, (screen_widt, screen_height))
