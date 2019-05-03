from enum import Enum
import pygame
pygame.init()
pygame.font.init()

screen_height = pygame.display.Info().current_h
screen_widt = pygame.display.Info().current_w
battlefield_width = screen_widt // 1.9
battlefield_height = screen_height // 3.5
battlefield_zero_point = (350, screen_height - 100)
N_x, N_y= 6, 6
cell_height = battlefield_height / N_y
H = 500


class person:
    def __init__(self, p_name, p_subject):
        self.name = p_name
        self.subject = p_subject
    def __eq__(self, other):
        if type(other) == person and self.subject == other.subject and self.name == other.name:
            return True
        else: return False


unitSpeed = 10
student_stat = 10
lecturer_knowlege_min = 9
lecturer_knwlege_max = 10
lecturer_easiness_min = 7
lecturer_easiness_max = 10
seminarist_knowlege_min = 7
seminarist_knwlege_max = 10
seminarist_easiness_min = 5
seminarist_easiness_max = 10
lecturer_friendliness_min = 0
lecturer_friendliness_max = 5
seminarist_friendliness_min = 0
seminarist_friendliness_max = 7
lecturer_alcohol_liking_min = 0
lecturer_alcohol_liking_max = 8
seminarist_alcohol_liking_min = 3
seminarist_alcohol_liking_max = 10
seminarists = dict()
subjects = ['matan', 'OKTCH', 'matlog']
seminarists['matan'] = (person('Ivanova', 'matan'), person('Kuzmenko', 'matan'), person('Starodubcev', 'matan'))
seminarists['OKTCH'] = (person('Grigoriev', 'OKTCH'), person('Glibenchuk', 'OKTCH'), person('Iliinskiy', 'OKTCH'))
seminarists['matlog'] = (person('Irhin', 'matlog'), person('Milovanov', 'matlog'), person('Ivachenko', 'matlog'))

lecturers_name = [person('Musatov', 'mathlog'), person('Raygor', 'OKTCH'),
                  person('Redkozubov', 'matan')]


class Subjects(Enum):
    OKTCH = 'OKTCH'
    matan = 'matan'
    matlog = 'matlog'


class Manager(Enum):
    bot = 'bot'
    player = 'player'

