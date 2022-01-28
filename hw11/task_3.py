"""
Реализуйте свойство класса, которое обладает следующим
функционалом: при установки значения этого свойства в файл с заранее
определенным названием должно сохранятся время (когда устанавливали
значение свойства) и установленное значение.
"""
from datetime import datetime


def write_to_txt_file(filename: str, content: str) -> None:
    with open(f'{filename}.txt', 'w') as f:
        f.write(content)


class WWW:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

        write_to_txt_file(self.name, str(datetime.now()))


class Point:
    x = WWW()
    y = WWW()

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


p = Point(4, 3)

p.x = 8
print(p)
