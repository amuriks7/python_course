"""
Дополните класс Группа (задание Лекции 2) возможностью поддержки
итерационного протокола
"""
from hw6.task1.group import Group
from hw6.task1.student import Student

if __name__ == '__main__':
    group = Group()

    for index in range(1, 11):
        group.add(
            Student(f'Petrov{index}', 19 + index, 'male', 4)
        )

    for student in group:
        print(student)
