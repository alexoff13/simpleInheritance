from humans import Human, Student


class Worker(Human):
    def __init__(self, weight, height, name, salary):
        super().__init__(weight, height, name)
        self.salary = salary

    def say(self):
        print('Привет, я офисный работник')


class OfficeWorker(Worker):
    def __str__(self):
        return f'Офисный работник по имени:{self.name}\nВес:{self._weight}\nРост{self._height}'


class Accountant(OfficeWorker):
    pass


class Sysadmin(OfficeWorker):
    pass


class WorkingStudent(Student, Worker):
    def __init__(self, weight, height, name, speciality, salary):
        super().__init__(weight, height, name, speciality)
        self.salary = salary
