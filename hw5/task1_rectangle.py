"""
Создайте класс «Прямоугольник», у которого присутствуют два поля
(ширина и высота). Реализуйте метод сравнения прямоугольников по
площади. Также реализуйте методы сложения прямоугольников (площадь
суммарного прямоугольника должна быть равна сумме площадей
прямоугольников, которые вы складываете). Реализуйте методы
умножения прямоугольника на число n (это должно увеличить площадь
базового прямоугольника в n раз).
"""


class Rectangle:

    def __init__(self, h: float, w: float):
        self.h = h
        self.w = w

    def __str__(self):
        return f'square is {self.h * self.w}'

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.h + other.h, self.w + other.w)
        else:
            return NotImplemented

    def __eq__(self, other):
        s1 = self.w * self.h
        s2 = other.w * other.h
        return s1 == s2

    def __gt__(self, other):
        s1 = self.w * self.h
        s2 = other.w * other.h
        return s1 > s2

    def __lt__(self, other):
        s1 = self.w * self.h
        s2 = other.w * other.h
        return s1 < s2

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Rectangle(self.h * other, other * self.w)
        else:
            return NotImplemented


if __name__ == '__main__':
    rectangle1 = Rectangle(2, 5)
    rectangle2 = Rectangle(3, 8)
    rectangle3 = rectangle1 * 5

    print(f'rectangle1 < rectangle2: {rectangle1 < rectangle2}')
    print(f'rectangle1 > rectangle2: {rectangle1 > rectangle2}')
    print(rectangle3)
