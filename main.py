from humans import Human, Student, OfficeWorker


def say(human: Human):
    human.say()
    print(human)


if __name__ == '__main__':
    human1 = Human(100, 170, 'Бешбармаш')
    human2 = Human(102, 171, 'Афанасий')
    human3 = Human(103, 172, 'Акакий')
    say(human1)
    student1 = Student(50, 165, 'Шизоид', 'IT')
    student2 = Student(50, 165, 'Андрей', 'Math')
    say(student2)
    office_worker = OfficeWorker(50, 150, 'Егор', 100)
    say(office_worker)
