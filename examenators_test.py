import examenator
import consts
import random


def test_lecturer():
    x = examenator.give_examenator_factory('lecturer', 10)
    y = x.create_examenator()
    z = consts.person(y.name, y.subject)
    scetchik = 0
    for i in range(consts.lecturers_name.__len__()):
        if consts.lecturers_name[i] == z:
            scetchik += 1
    assert scetchik == 1
    assert type(y.knowlege) == int
    assert type(y.easiness) == int
    assert type(y.friendliness) == int
    assert type(y.alcohol_liking) == int


def test_seminarist():
    x = examenator.give_examenator_factory('seminarist', 10)
    y = x.create_examenator()
    z = consts.person(y.name, y.subject)
    p = 0
    for i in range(consts.seminarists[y.subject].__len__()):
        if consts.seminarists[y.subject][i] == z:
            p += 1
    assert p == 1
    assert type(y.knowlege) == int
    assert type(y.easiness) == int
    assert type(y.friendliness) == int
    assert type(y.alcohol_liking) == int


for i in range(10000):
    test_lecturer()
    test_seminarist()
