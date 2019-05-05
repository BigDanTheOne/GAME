from students import *
import consts


def test_student():
    factory = giveStudentFacroty('bot', 'DIHT', 2)
    unit = factory.createUnit()
    assert unit.faculty == 'DIHT'
    assert type(unit.intelect) == int
    assert type(unit.friendliness) == int
    assert type(unit.luck) == int
    assert type(unit.oratory) == int
    assert unit.sex in ('man', 'not man')


for i in range(10000):
    test_student()
