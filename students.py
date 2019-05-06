from consts import *
from renderer import *
import images
import random
import pygame
import math
import copy
class Bilet:
    global subjects
    def __init__(self, add_quastion):
        if add_quastion == True:
            self.topic = None
            self.task1 = random.choice(subjects)
        else:
            self.topic = random.choice(subjects)
            self.task1 = random.choice(subjects)
            self.task2 = random.choice(subjects)


class Menu:
    def __init__(self, given_player, dificulty):
        self.dificulty = dificulty
        self.player = given_player
        self.end = False
        #TODO: calling the griphical interface of Menu

    def getParametr(self):
        'info we got froom the griphical interface'
        while True:
            print('choose one of these:'
                  'luck from 0 to {} '
                  'frequency  from 0 to {} '
                  'time_bot from 0 to {} '
                  'alcohol from 0 to {} '
                  'if the choice is done print exit 0'.format(int(10 / self.dificulty), int(10 / self.dificulty), int(10 / self.dificulty), int(10 / self.dificulty)))
            type, value = input().split()
            if type == 'exit':
                self.end = True
                break
            if type not in ('luck', 'frequency', 'time_bot', 'alcohol') and int(value) not in range(int(10 / self.dificulty)):
                print('incorrect input')
            else:
                break
        return type, int(value)


class BBox:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.r = radius

    def intersection(self, x : int, y : int):
        if (x - self.x)**2 + (y - self.y)**2 <= self.r**2:
            return True
        else:
            return False


class Unit:
    def __init__(self, imgHead, imgBody):
        self.bbox: BBox = BBox(100, 100, 10)
        self.speed: int = unitSpeed
        self.imgHead:  pygame.Surface = images.student_head
        self.imgBody:  pygame.Surface = images.student_body
        self.imgBody0: pygame.Surface = images.student_body
        self.w_0: int = self.imgBody.get_size()[0]
        self.h_0: int = self.imgBody.get_size()[1]
        self.target: BBox = BBox(-1, -1, 0)
        self.moving: bool = False

    def rescale(self):
        self.imgBody = pygame.transform.scale(self.imgBody0, (int(self.w_0 * (H - battlefield_zero_point[1] + self.bbox.y) // H),
                                                            int(self.h_0 * (H - battlefield_zero_point[1] + self.bbox.y) // H)))
    def distance_to_target(self):
        return math.sqrt((self.target.x - self.bbox.x)**2 + (self.target.y - self.bbox.y)**2)

    def step(self, delta_t):
        if self.moving:

            new_bbox = copy.deepcopy(self.bbox)
            print(self.bbox.x, self.bbox.y)
            new_bbox.x += self.speed * math.sin(math.atan2(self.target.x - self.bbox.x, self.target.y - self.bbox.y)) * delta_t
            new_bbox.y += self.speed * math.cos(math.atan2(self.target.x - self.bbox.x, self.target.y - self.bbox.y)) * delta_t
            # Checking that the target is achieved
            if self.distance_to_target() < self.speed * delta_t:
                self.moving = False
                new_bbox = copy.deepcopy(self.target)
                self.target.x= self.target.y= -1

            self.bbox = new_bbox

            # Jumping animation
            #self.spriteoffset = 2 * ((self.time * 20) % 5)
        #self.time += delta_t


    def go_to(self, target):
        self.target = BBox(target[0], target[1], 0)
        self.moving = True
        self.time = 0

    def intersection(self, x : int, y : int):
        return self.bbox.intersection(x, y)




class Student(Unit):
    def __init__(self):
        imgBody = images.student_body
        imgHead = images.student_head
        super().__init__(imgHead, imgBody)
        self.stats = dict()
        #print('I am a Student')
    def answer(self, bilet):
        pass

    def  askAnswer(self, student, bilet):
        pass

    def giveAnswer(self, student,bilet):
        pass

    def giveStats(self):
        'There we have some formula, which computes stats, now its only simple sum'
        ans = 0
        #print(self.stats)
        for i in self.stats:
            if i != 'faculty':
                ans+= int(self.stats[i])
        return ans

    def select_unit(self, unit : Unit):
        pass

    
    
    
    

class Player(Student):
    def __init__(self, *args):
        #TODO: add default stats
        super().__init__()
        #print('I am a Student')



class Bot(Student):
    def __init__(self, faculty, difficulty):
        super().__init__()
        #print('I am a Bot')
        self.faculty = faculty
        self.luck = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.intelect = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.oratory = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.sex = random.choice(('man', 'not man'))
        self.friendliness = int(random.normalvariate(student_stat / difficulty, 2) % 10)
        self.stats['faculty'] = self.faculty
        self.stats['luck'] = self.luck
        self.stats['faculty'] = self.faculty
        self.stats['intelect'] = self.intelect
        self.stats['oratory'] = self.oratory
        self.stats['sex'] = self.sex
        self.stats['friendliness'] = self.friendliness
        #TODO: add skills


class BotFactory:
    'there you can choose a Faculty and a difficulty of the game from 1 to 5'
    'the higher the complexity the lower the characteristics of the allies'
    def __init__(self, faculty, difficulty):
        self.faculty = faculty
        self.difficulty = difficulty

    def createUnit(self):
        return Bot(self.faculty, self.difficulty)



class PlayerFactory:
    class builder:
        def __init__(self, player, menu):
            self.player = player
            self.menu = menu

        def fillField(self):
            type, value = self.menu.getParametr()
            if type != 'exit':
                # self.Player.type = value
                self.player.stats[type] = value
            print('now your total power is: ', self.player.giveStats())


    def __init__(self,  faculty, difficulty):
        self.my_player= Player()
        self.my_menu = Menu(self.my_player, difficulty)
        self.my_builder = PlayerFactory.builder(self.my_player, self.my_menu)
        self.my_player.faculty = faculty
        self.my_player.stats['faculty'] = faculty
        while self.my_menu.end != True:
            self.my_builder.fillField()

    def createUnit(self):
        return self.my_player


def giveStudentFacroty(manager, facuty, difficulty):
    'args for manager: "manager.layer", "manager.bot"'
    if manager == manager.player:
        return PlayerFactory(facuty, difficulty)
    elif manager == manager.bot:
        return BotFactory(facuty, difficulty)
    else:
        raise TypeError

#my_factory1 = giveStudentFacroty('Bot', 'DIHT', 2)
#my_factory2 = giveStudentFacroty('Player', 'DIHT', 2)
#my_bot = my_factory1.createUnit()
#my_player = my_factory2.createUnit()
#print(my_bot.__dict__)
#print(my_player.__dict__)

