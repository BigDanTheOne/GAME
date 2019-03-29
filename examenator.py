import random
import consts


class examenator:
    def __str__(self):
        return '{}, name = {}, subject = {}, knowlege = {}, easiness = {}, alcohol_liking = {}, friendliness = {}'.format(
            self.type, self.name, self.subject,
            self.knowlege, self.easiness, self.alcohol_liking, self.friendliness)


class lecturer(examenator):
    type = 'lecturer'


class seminarist(examenator):
    type = 'seminarist'


class lecturers_factory:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def create_examenator(self):
        lecturer_1 = lecturer()
        lecturer_1.knowlege = int(random.normalvariate(consts.lecturer_knowlege / self.difficulty, 2) % 10)
        lecturer_1.easiness = int(random.normalvariate(consts.lecturer_easiness / self.difficulty, 2) % 10)
        lecturer_1.friendliness = int(random.normalvariate(consts.lecturer_friendliness / self.difficulty, 2) % 10)
        lecturer_1.friendliness = int(random.normalvariate(consts.lecturer_friendliness / self.difficulty, 2) % 10)
        lecturer_1.alcohol_liking = int(random.normalvariate(consts.lecturer_alcohol_liking / self.difficulty, 2) % 10)
        y = random.randint(0, consts.lecturers_name.__len__() - 1)
        lecturer_1.name = consts.lecturers_name[y].name
        lecturer_1.subject = consts.lecturers_name[y].subject
        return lecturer_1


class seminarists_factory:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def create_examenator(self, subject=consts.subjects[random.randint(0, consts.subjects.__len__() - 1)]):
        seminarist_1 = seminarist()
        seminarist_1.knowlege = int(random.normalvariate(consts.seminarist_knowlege / self.difficulty, 2) % 10)
        seminarist_1.easiness = int(random.normalvariate(consts.seminarist_easiness / self.difficulty, 2) % 10)
        seminarist_1.friendliness = int(random.normalvariate(consts.seminarist_friendliness / self.difficulty, 2) % 10)
        seminarist_1.alcohol_liking = int(
            random.normalvariate(consts.seminarist_alcohol_liking / self.difficulty, 2) % 10)
        a = consts.seminarists[subject][random.randint(0, consts.seminarists[subject].__len__() - 1)]
        seminarist_1.name = a.name
        seminarist_1.subject = a.subject
        return seminarist_1


def give_examenator_factory(examenator, *args):
    if examenator == 'lecturer':
        return lecturers_factory(*args)
    elif examenator == 'seminarist':
        return seminarists_factory(*args)

