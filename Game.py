from enum import Enum
from consts import *
import pygame
import random
from pygame import *
from consts import *
from images import *
import Comand
import pygame.locals
from renderer import *
from students import *
import random

pygame.init()
pygame.font.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_widt, screen_height))
        self.battlefield = pygame.Surface((screen_widt, screen_height), pygame.SRCALPHA)
        self.action_scene = pygame.Surface((screen_widt, screen_height), pygame.SRCALPHA)
        self.static_scene = pygame.Surface((screen_widt, screen_height), pygame.SRCALPHA)
        self.run = True
        self.battlefield.blit(background, (0, 0))
        self.renderer = Renderer(self.battlefield, self.action_scene, self.screen, self.static_scene)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT or \
                    (event.type == pygame.locals.KEYDOWN and
                     event.key == pygame.locals.K_ESCAPE):
                return False
        return True

    def preparing_units(self, map: Map):
        x = giveStudentFacroty('Bot', random.choice(subjects), 5)
        s = [x.createUnit(), x.createUnit(), x.createUnit()]
        tmp = [[False for j in range(N_x)] for i in range(N_y)]
        for i in s:
            while True:
                cell_x, cell_y = random.randint(0, N_x - 1), random.randint(0, N_y - 1)
                if not tmp[cell_x][cell_y]:
                    tmp[cell_x][cell_y] = True
                    i.bbox.x, i.bbox.y = map.get_x_y_by_cell(cell_x, cell_y)
                    break
        return s, []

    def play(self):
        pygame.display.set_caption("Phistech.Battle")
        map = Map()
        students, examinators = self.preparing_units(map)
        self.renderer.render_background()
        self.renderer.render_map(map)
        self.renderer.render_all_units(students)
        self.renderer.update_screen(self.screen)
        while self.run:
            for student in students:
                events = pygame.event.get()
                student.draw_menu(self.screen)
                for event in events:
                    self.renderer.render_highlighted_cells(map)
                    if event.type == pygame.QUIT:
                        self.run = False
                action = map.recognize_action(students, events)
                if type(action) == Comand.Exit:
                    self.run = False
                    continue
                elif type(action) == Comand.GoTo:
                    student.go_to((action.x, action.y))
                    self.renderer.render_going_unit(student, (action.x, action.y), students)
                    pygame.display.update()
                    continue

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.play()
