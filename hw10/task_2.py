"""
Создайте декоратор класса с параметром. Параметром должна быть
строка, которая должна дописываться (слева) к результату работы метода
__str__.
"""
from functools import wraps


def optimize_str(string: str):
    def _inner(cls):
        old_str = cls.__str__

        @wraps(cls.__str__)
        def decorated_str(self, *args, **kwargs):
            result = old_str(self, *args, **kwargs)
            return f'{string} {result}'

        cls.__str__ = decorated_str
        return cls

    return _inner


@optimize_str('Super')
class Car:
    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year

    def __str__(self):
        return f'{self.model} {self.year}'


car = Car('BMW', 2021)

print(car)
