class Human:
    def __init__(self, surname, age, gender):
        self.surname = surname
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.surname}, age: {self.age}, gender: {self.gender}'
