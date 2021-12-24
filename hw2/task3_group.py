""" Создайте класс Группа, который содержит массив из 10
объектов класса Студент. Реализуйте методы добавления,
удаления студента и метод поиска студента по фамилии.
Определите для Группы метод __str__() для возвращения списка
студентов в виде строки."""

from task2_student import Student


class Group:
    def __init__(self):
        self.student_list = []

    def add(self, student: Student):
        self.student_list.append(student)

    def delete(self, student: Student):
        self.student_list.remove(student)

    def search(self, student_surname: str) -> str:
        result = f'Нет такой фамилии {student_surname}'
        for i in self.student_list:
            if student_surname == i.surname:
                result = f'Есть такая фамилия {student_surname}'
                break
        return result

    def __str__(self):
        result = "\n"
        j = 1
        for student in self.student_list:
            result += f'{j} {student}'
            j = j + 1

        return 'Student list:' + result


if __name__ == '__main__':
    group = Group()

    for index in range(1, 11):
        group.add(
            Student(f'Petrov{index}', 20, 'male', 4)
        )

    print(group)

    student_for_deleting = group.student_list[9]
    group.delete(student_for_deleting)

    print(group)

    print(group.search('Petrov1'))
    print(group.search('Petrovskiy'))
