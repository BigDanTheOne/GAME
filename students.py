from consts import *
from renderer import *
from unit import *
import images
import random
import pygame
import math
import copy



class Menu:
    def __init__(self, given_player):
        self.player = given_player
        self.end = False
        # TODO: calling the griphical interface of Menu

    def getParametr(self, dificulty):
        'info we got froom the griphical interface'
        while True:
            print('choose one of these:\nluck from 0 to {}\nintelect  from 0 to {}\noratory from 0 to {}\nfriendliness from 0 to {}\nif the choice is done print exit 0'.format(int(10 / dificulty), int(10 / dificulty),
                                                              int(10 / dificulty), int(10 / dificulty)))
            type, value = input().split()
            if type == 'exit':
                self.end = True
                break
            if type not in ('luck', 'frequency', 'time_bot', 'alcohol', 'exit') and int(value) not in range(
                    int(10 / dificulty)):
                print('incorrect input')
            else:
                break
        return type, int(value)


class BBox:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.r = radius

    def intersect(self, x: int, y: int):
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2


class Student(Unit):
    def __init__(self):
        self.type = 'student'
        self.stats = dict()
        super().__init__()
        # print('I am a Student')

    def giveStats(self):
        'There should be some formula, which computes stats, now its only simple stats'
        return self.stats


class Player(Student):
    def __init__(self, *args):
        super().__init__()
        self.imgBody = body['player']
        self.subject = ""
        self.luck = 0
        self.intelect = 0
        self.oratory =  0
        self.sex = random.choice(('man', 'woman'))
        self.friendliness = 0
        self.stats['subject'] = ""
        self.stats['luck'] = 0
        self.stats['intelect'] = 0
        self.stats['oratory'] = 0
        self.stats['sex'] = self.sex
        self.stats['friendliness'] = 0


class Bot(Student):
    def __init__(self, difficulty):
        # print('I am a Bot')
        super().__init__()
        self.subject = random.choice(subjects)
        self.luck = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.intelect = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.oratory = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.sex = random.choice(('man', 'woman'))
        self.friendliness = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.stats['subject'] = self.subject
        self.stats['luck'] = self.luck
        self.stats['intelect'] = self.intelect
        self.stats['oratory'] = self.oratory
        self.stats['friendliness'] = self.friendliness


class BotFactory:
    'there you can choose a Favourity subject and a difficulty of the game from 1 to 5'
    'the higher the complexity the lower the characteristics of the allies'

    def __init__(self, subject, difficulty):
        self.subject = subject
        self.difficulty = difficulty

    def createUnit(self):
        return Bot(self.difficulty)


class PlayerFactory:
    class builder:
        def __init__(self, player, menu):
            self.player = player
            self.menu = menu

        def fillField(self, difficulty):
            try:
                type, value = self.menu.getParametr(difficulty)
            except BaseException:
                print('incorrect input')
                return
            if type not in ('luck', 'intelect', 'oratory', 'sex', 'friendliness', 'exit') or value not in range(int(10 // difficulty + 1)):
                print('incorrect input')
            else:
                if type != 'exit':
                    # self.Player.type = value
                    self.player.stats[type] = value
                print('now your stats are: ', self.player.giveStats())

    def __init__(self, subject, difficulty):
        self.my_player = Player()
        self.my_menu = Menu(self.my_player)
        self.my_builder = PlayerFactory.builder(self.my_player, self.my_menu)
        self.my_player.subject = subject
        self.my_player.stats['subject'] = subject
        while not self.my_menu.end:
            self.my_builder.fillField(difficulty)

    def createUnit(self):
        self.my_player.subject = self.my_player.stats['subject']
        self.my_player.luck = self.my_player.stats['luck']
        self.my_player.intelect = self.my_player.stats['intelect']
        self.my_player.oratory = self.my_player.stats['oratory']
        self.my_player.friendliness = self.my_player.stats['friendliness']
        return self.my_player


def giveStudentFacroty(manager, subject, difficulty):
    'args for manager: "Player", "Bot"'
    # print('creating an abstract Student')
    if manager == 'Player':
        return PlayerFactory(subject, difficulty)
    elif manager == 'Bot':
        return BotFactory(subject, difficulty)
    else:
        raise TypeError