"""На его основе создайте класс Студент (переопределите метод
вывода информации)."""
from hw2.task1_human import Human


class Student(Human):
    def __init__(self, surname, age, gender, course):
        super().__init__(surname, age, gender)
        self.course = course

    def __str__(self):
        return f'Student: {super().__str__()}, course: {self.course}'


if __name__ == '__main__':
    student_1 = Student('Petrov', 20, 'male', 2)
    student_2 = Student('Lisman', 21, 'male', 1)

    print(student_1)
    print(student_2)
