from hw4.exceptions import TooManyStudentsInGroupException
from hw4.student import Student


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