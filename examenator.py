import random
from strategy import *
from unit import *
from consts import *


class examenator(Unit):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return '{}, name = {}, subject = {}, knowlege = {}, easiness = {}, alcohol_liking = {}, friendliness = {}, sex = {}'.format(
            self.type, self.name, self.subject,
            self.knowlege, self.easiness, self.alcohol_liking, self.friendliness, self.sex)


class lecturer(examenator):
    type = 'lecturer'
    def __init__(self):
        super().__init__()

class seminarist(examenator):
    type = 'seminarist'
    def __init__(self):
        super().__init__()


class lecturers_factory:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def create_examenator(self):
        lec = lecturer()
        lec.knowlege = int(random.normalvariate(lecturer_knowlege / self.difficulty, 2) % max_stat)
        lec.easiness = int(random.normalvariate(lecturer_easiness / self.difficulty, 2) % max_stat)
        lec.friendliness = int(random.normalvariate(lecturer_friendliness / self.difficulty, 2) % max_stat)
        lec.alcohol_liking = int(random.normalvariate(lecturer_alcohol_liking / self.difficulty, 2) % max_stat)
        y = random.randint(0, lecturers_name.__len__() - 1)
        lec.name = lecturers_name[y].name
        lec.face = lecturers_name[y].picture
        lec.subject = lecturers_name[y].subject
        lec.sex = lecturers_name[y].sex
        lec.stats = {'name': lec.name, 'knowlege': lec.knowlege, 'easiness': lec.easiness,
                     'friendliness': lec.friendliness,
                     'alcohol_liking': lec.alcohol_liking, 'subject': lec.subject, 'sex': lec.sex}
        return lec


class seminarists_factory:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def create_examenator(self, subject=subjects[random.randint(0, subjects.__len__() - 1)]):
        sem = seminarist()
        sem.knowlege = int(random.normalvariate(seminarist_knowlege / self.difficulty, 2) % max_stat)
        sem.easiness = int(random.normalvariate(seminarist_easiness / self.difficulty, 2) % max_stat)
        sem.friendliness = int(random.normalvariate(seminarist_friendliness / self.difficulty, 2) % max_stat)
        sem.alcohol_liking = int(
            random.normalvariate(seminarist_alcohol_liking / self.difficulty, 2) % max_stat)
        a = seminarists[subject][random.randint(0, seminarists[subject].__len__() - 1)]
        sem.face = a.picture
        sem.name = a.name
        sem.subject = a.subject
        sem.sex = a.sex
        sem.stats = {'name': sem.name, 'knowlege': sem.knowlege, 'easiness': sem.easiness,
                     'friendliness': sem.friendliness,
                     'alcohol_liking': sem.alcohol_liking, 'subject': sem.subject, 'sex': sem.sex}
        return sem


def give_examenator_factory(examenator, *args):
    if examenator == 'lecturer':
        return lecturers_factory(*args)
    elif examenator == 'seminarist':
        return seminarists_factory(*args)
