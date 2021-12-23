"""Создайте класс, описывающий человека (создайте метод,
выводящий информацию о человеке)."""


class Human:
    def __init__(self, surname, age, gender):
        self.surname = surname
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.surname}, age: {self.age}, gender: {self.gender}'


if __name__ == '__main__':
    human_1 = Human('Ivanov', 20, 'male')
    print(human_1)
