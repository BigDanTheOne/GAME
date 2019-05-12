import random
from strategy import *
from unit import *
from consts import *


class examenator(Unit):
    def __init__(self):
        super().__init__()


class lecturer(examenator):
    type = 'lecturer'
    def __init__(self, difficulty):
        self.stats = dict()
        super().__init__()
        self.difficulty = difficulty
        self.knowlege = int(random.normalvariate(lecturer_knowlege / self.difficulty, 2) % max_stat)
        self.easiness = int(random.normalvariate(lecturer_easiness / self.difficulty, 2) % max_stat)
        self.friendliness = int(random.normalvariate(lecturer_friendliness / self.difficulty, 2) % max_stat)
        self.alcohol_liking = int(random.normalvariate(lecturer_alcohol_liking / self.difficulty, 2) % max_stat)
        y = random.randint(0, lecturers_name.__len__() - 1)
        self.name = lecturers_name[y].name
        self.face = lecturers_name[y].picture
        self.subject = lecturers_name[y].subject
        self.sex = lecturers_name[y].sex
        self.stats.update({'name': self.name, 'knowlege': self.knowlege, 'easiness': self.easiness,
                     'friendliness': self.friendliness,
                     'alcohol_liking': self.alcohol_liking, 'subject': self.subject, 'sex': self.sex})

class seminarist(examenator):
    type = 'seminarist'
    def __init__(self, difficulty, subject):
        self.stats = dict()
        super().__init__()
        self.difficulty = difficulty
        self.knowlege = int(random.normalvariate(seminarist_knowlege / self.difficulty, 2) % max_stat)
        self.easiness = int(random.normalvariate(seminarist_easiness / self.difficulty, 2) % max_stat)
        self.friendliness = int(random.normalvariate(seminarist_friendliness / self.difficulty, 2) % max_stat)
        self.alcohol_liking = int(
            random.normalvariate(seminarist_alcohol_liking / self.difficulty, 2) % max_stat)
        a = seminarists[subject][random.randint(0, seminarists[subject].__len__() - 1)]
        self.face = a.picture
        self.name = a.name
        self.subject = a.subject
        self.sex = a.sex
        self.stats.update({'name': self.name, 'knowlege': self.knowlege, 'easiness': self.easiness,
                     'friendliness': self.friendliness,
                     'alcohol_liking': self.alcohol_liking, 'subject': self.subject, 'sex': self.sex})


class lecturers_factory:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def createUnit(self):
        lec = lecturer(self.difficulty)
        return lec


class seminarists_factory:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def createUnit(self, subject=subjects[random.randint(0, subjects.__len__() - 1)]):
        sem = seminarist(self.difficulty, subject)
        return sem


def give_examenator_factory(examenator, *args):
    if examenator == 'lecturer':
        return lecturers_factory(*args)
    elif examenator == 'seminarist':
        return seminarists_factory(*args)
