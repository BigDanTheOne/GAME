class person:
    def __init__(self, p_name, p_subject):
        self.name = p_name
        self.subject = p_subject
    def __eq__(self, other):
        if type(other) == person and self.subject == other.subject and self.name == other.name:
            return True
        else: return False

lecturer_knowlege = 10
lecturer_easiness = 10
seminarist_knowlege = 10
seminarist_easiness = 10
lecturer_friendliness = 10
seminarist_friendliness = 10
lecturer_alcohol_liking = 10
seminarist_alcohol_liking = 10
student_stat = 10
seminarists = dict()
subjects = ['matan', 'OKTCH', 'matlog']
seminarists['matan'] = (person('Ivanova', 'matan'), person('Kuzmenko', 'matan'), person('Starodubcev', 'matan'))
seminarists['OKTCH'] = (person('Grigoriev', 'OKTCH'), person('Glibenchuk', 'OKTCH'), person('Iliinskiy', 'OKTCH'))
seminarists['matlog'] = (person('Irhin', 'matlog'), person('Milovanov', 'matlog'), person('Ivachenko', 'matlog'))

lecturers_name = [person('Musatov', 'mathlog'), person('Raygor', 'OKTCH'),
                  person('Redkozubov', 'matan')]
