from humans.human import Human


class Student(Human):

    def __init__(self, weight, height, name, speciality):
        super().__init__(weight, height, name)
        self.speciality = speciality

    def say(self):
        print('Привет, я студент')

    def __str__(self):
        return f'Студент по имени:{self.name}\nВес:{self._weight}\nРост{self._height}'
