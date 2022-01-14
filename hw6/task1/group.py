from hw6.task1.student import Student


class GroupIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index = self.index + 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


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

    def __iter__(self):
        return GroupIterator(self.student_list)


