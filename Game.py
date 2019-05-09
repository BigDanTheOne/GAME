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
from examenator import *
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
        self.map = Map()
        self.cells = [[False for j in range(N_x)] for i in range(N_y)]
        self.battlefield.blit(background, (0, 0))
        self.renderer = Renderer(self.battlefield, self.action_scene, self.screen, self.static_scene)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT or \
                    (event.type == pygame.locals.KEYDOWN and
                     event.key == pygame.locals.K_ESCAPE):
                return False
        return True

    def preparing_units(self, map: Map, students, lecturers, seminarists, difficulty):
        stud_f = giveStudentFacroty('Bot', random.choice(subjects), difficulty)
        lec_f = lecturers_factory(difficulty)
        sem_f = seminarists_factory(difficulty)
        self.units = []
        self.units += ([stud_f.createUnit() for i in range(students)])
        self.units += ([lec_f.createUnit() for i in range(lecturers)])
        self.units += ([sem_f.createUnit() for i in range(seminarists)])
        for i in self.units:
            while True:
                cell_x, cell_y = random.randint(0, N_x - 1), random.randint(0, N_y - 1)
                if not self.cells[cell_x][cell_y]:
                    self.cells[cell_x][cell_y] = True
                    i.bbox.x, i.bbox.y = self.map.get_x_y_by_cell(cell_x, cell_y)
                    break

    def update_cells(self, from_x, from_y, to_x, to_y):
        self.cells[from_x][from_y] = False
        self.cells[to_x][to_y] = True

    def check_go(self, unit, c_x, c_y, action, student):
        unit_x, unit_y = self.map.get_cell_by_x_y(unit.bbox.x, unit.bbox.y)
        to_x, to_y = self.map.get_cell_by_x_y(action.x, action.y)
        if not self.cells[to_x][to_y] and abs(c_x - to_x) + abs(c_y - to_y) < dist:
            self.update_cells(unit_x, unit_y, to_x, to_y)
            student.go_to((action.x, action.y))
            self.renderer.render_going_unit(student, (action.x, action.y), self.units)
            return True
        return False

    def action(self, unit1, unit2):
        cell1_x, cell1_y = self.map.get_cell_by_x_y(unit1.bbox.x, unit1.bbox.y)
        cell2_x, cell2_y = self.map.get_cell_by_x_y(unit2.bbox.x, unit2.bbox.y)
        if abs(cell1_x - cell2_x) < 2 and abs(cell1_y - cell2_y) < 2 :
            if unit1.type == unit2.type:
                hill1(unit1, unit2)
            elif unit1.type != 'student' and unit2.type != 'student':
                hill1(unit1, unit2)
            else:
                hit = hit1(unit1, unit2, unit1.type)
                unit2.health -= hit
                unit2.stats['health'] -= hit
                if unit2.health <= 0:
                    for i in range(len(self.units)):
                        if self.units[i] == unit2:
                            x , y = self.map.get_cell_by_x_y(unit2.bbox.x, unit2.bbox.y)
                            self.cells[x][y] = False
                            del(self.units[i])
                            self.renderer.render_all_units(self.units)
                            break
            return True
        return False

    def students_turn(self):
        for student in self.units:
            if student.type != 'student' or not self.run:
                continue
            this_student = True
            my_cell_x, my_cell_y = self.map.get_cell_by_x_y(student.bbox.x, student.bbox.y)
            while this_student:
                self.renderer.render_highlighted_cells(self.map, my_cell_x, my_cell_y, self.cells, dist, student)

                events = pygame.event.get()
                for event in events:
                    self.renderer.render_all_units(self.units)
                    pygame.display.update()
                    if event.type == pygame.QUIT:
                        self.run = False
                        this_student = False
                        continue
                action = self.map.recognize_action([student], events)
                if type(action) == Comand.Exit:
                    self.run = False
                    this_student = False
                    continue
                elif type(action) == Comand.GoTo:
                    if self.check_go(student, my_cell_x, my_cell_y, action, student):
                        self.renderer.render_all_units(self.units)
                    else:
                        for unit in self.units:
                            if unit.bbox.x == action.x and unit.bbox.y == action.y:
                                if self.action(student, unit):
                                    this_student = False
                                    break
                    pygame.display.update()
                elif type(action) == bool:
                    this_student = False
                    continue

                pygame.display.update()

    def play(self):
        pygame.display.set_caption("Phystech.Battle")
        self.preparing_units(self.map, 3, 1, 1, 1)
        self.renderer.render_background()
        self.renderer.render_map(self.map)
        self.renderer.render_all_units(self.units)
        self.renderer.update_screen(self.screen)
        while self.run:
            for unit in self.units:
                self.students_turn()
                # events = pygame.event.get()
                # unit.draw_menu(self.screen)
                # for event in events:
                #     self.renderer.render_highlighted_cells(self.map)
                #     if event.type == pygame.QUIT:
                #         self.run = False
                # action = self.map.recognize_action(self.units, events)
                # if type(action) == Comand.Exit:
                #     self.run = False
                #     continue
                # elif type(action) == Comand.GoTo:
                #     unit.go_to((action.x, action.y))
                #     self.renderer.render_going_unit(unit, (action.x, action.y), self.units)
                #     pygame.display.update()
                #     continue


if __name__ == '__main__':
    game = Game()
    game.play()
