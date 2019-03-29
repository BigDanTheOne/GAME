import consts
topics = tuple(consts.subjects)

import random
class bilet:
    global topics
    def __init__(self, add_quastion):
        if add_quastion == True:
            self.topic = None
            self.task1 = random.choice(topics)
        self.topic = random.choice(topics)
        self.task1 = random.choice(topics)
        self.task2 = random.choice(topics)


class builder:
    def __init__(self, player, menu):
        self.player = player
        self.menu = menu

    def fillField(self):
        type, value = self.menu.getParametr()
        if type != 'exit':
            #self.player.type = value
            self.player.stats[type] = value
        print('now your total power is: ', self.player.giveStats())





class menu:
    def __init__(self, given_player, dificulty):
        self.dificulty = dificulty
        self.player = given_player
        self.end = False
        #TODO: calling the griphical interface of menu

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


class unit:
    def __init__(self):
        self.stats = dict()
        print('I am a unit')
    def answer(self, bilet):
        pass

    def move(self, whereToGo):
        pass

    def  askAnswer(self, student, bilet):
        pass

    def giveAnswer(self, student,bilet):
        pass

    def giveStats(self):
        'There we have some formula, which computes stats, now its onlt simple sum'
        ans = 0
        #print(self.stats)
        for i in self.stats:
            if i != 'faculty':
                ans+= int(self.stats[i])
        return ans

class player(unit):
    def __init__(self, *args):
        #TODO: add default stats
        super().__init__()
        print('I am a student')



class bot(unit):
    def __init__(self, faculty, difficulty):
        super().__init__()
        print('I am a bot')
        self.faculty = faculty
        self.luck = int(random.normalvariate(10 / difficulty, 2) % 10)
        self.intelect = int(random.normalvariate(10 / difficulty, 2) % 10)
        self.oratory = int(random.normalvariate(10 / difficulty, 2) % 10)
        self.sex = int(random.random() % 2)
        self.friendliness = int(random.normalvariate(10 / difficulty, 2) % 10)
        self.stats['faculty'] = self.faculty
        self.stats['luck'] = self.luck
        self.stats['faculty'] = self.faculty
        self.stats['intelect'] = self.intelect
        self.stats['oratory'] = self.oratory
        self.stats['sex'] = self.sex
        self.stats['friendliness'] = self.friendliness
        #TODO: add skills


class botFactory:
    'there you can choose a Faculty and a difficulty of the game from 1 to 5'
    'the higher the complexity the lower the characteristics of the allies'
    def __init__(self, faculty, difficulty):
        self.faculty = faculty
        self.difficulty = difficulty

    def createUnit(self):
        return bot(self.faculty, self.difficulty)


class playerFactory:
    def __init__(self,  faculty, difficulty):
        self.my_player= player()
        self.my_menu = menu(self.my_player, difficulty)
        self.my_builder = builder(self.my_player, self.my_menu)
        self.my_player.faculty = faculty
        self.my_player.stats['faculty'] = faculty
        while self.my_menu.end != True:
            self.my_builder.fillField()

    def createUnit(self):
        return self.my_player


def giveStudentFacroty(manager, *args):
    'args for manager: p - player, b - bot'
    'if bot: *args = faculty, difficulty'
    print('creating an abstract student')
    if manager == 'p':
        return playerFactory(*args)
    elif manager == 'b':
        return botFactory(*args)
    else:
        raise TypeError

my_factory1 = giveStudentFacroty('b', 'DIHT', 2)
my_factory2 = giveStudentFacroty('p', 'DIHT', 2)
my_bot = my_factory1.createUnit()
my_player = my_factory2.createUnit()
print(my_bot.__dict__)
print(my_player.__dict__)

