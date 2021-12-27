"""
Модифицируйте класс Группа (задание прошлой лекции) так, чтобы при
попытке добавления в группу более 10-ти студентов, было возбужденно
пользовательское исключение. Таким образом нужно создать еще и
пользовательское исключение для этой ситуации. И обработать его.
"""


class TooManyStudentsInGroupException(Exception):
    def __init__(self, message):
        self.message = message


class Human:
    def __init__(self, surname, age, gender):
        self.surname = surname
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.surname}, age: {self.age}, gender: {self.gender}'


class Student(Human):
    def __init__(self, surname, age, gender, course):
        super().__init__(surname, age, gender)
        self.course = course

    def __str__(self):
        return f'Student: {super().__str__()}, course: {self.course}'


class Group:
    def __init__(self):
        self.student_list = []

    def add(self, student: Student):
        if len(self.student_list) > 10:
            raise TooManyStudentsInGroupException("Error! Max students number in group - 10!")
        else:
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
        res = '\n\t'.join(map(str, self.student_list))

        return f'Student list:\n\t{res}'


if __name__ == '__main__':
    group = Group()

    try:
        for index in range(1, 13):
            group.add(
                Student(f'Petrov{index}', 19 + index, 'male', 4)
            )
    except TooManyStudentsInGroupException as e:
        print(group)
        print(e.message)
    else:
        print(group)
