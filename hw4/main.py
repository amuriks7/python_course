"""
Разнесите классы, которые использовали при решении задачи о группе
студентов (задания прошлой лекции) по модулям. Убедитесь в
работоспособности проекта.
"""
from hw4.exceptions import TooManyStudentsInGroupException
from hw4.group import Group
from hw4.student import Student

if __name__ == '__main__':
    group = Group()

    try:
        for index in range(1, 12):
            group.add(
                Student(f'Petrov{index}', 19 + index, 'male', 4)
            )
    except TooManyStudentsInGroupException as e:
        print(group)
        print(e.message)
    else:
        print(group)
