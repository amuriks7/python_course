import human


class Student(human.Human):
    def __init__(self, surname, age, gender, course):
        super().__init__(surname, age, gender)
        self.course = course

    def __str__(self):
        return f'Student: {super().__str__()}, course: {self.course}'
