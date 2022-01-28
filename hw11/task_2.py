"""
Реализуйте функционал, который будет запрещать установку полей класса
любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
попытаться присвоить, например, строку, то должно быть возбужденно
исключение.
"""


class IntOnlyProperty:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise AttributeError("Incorrect data type.")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = IntOnlyProperty()
    y = IntOnlyProperty()

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


p = Point(2, 3)
print(p)

p.x = 5
print(p)

try:
    p.x = 4.2
except AttributeError as e:
    print(e)
    print(p.x)
