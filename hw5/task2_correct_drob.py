"""
Создайте класс «Правильная дробь» и реализуйте методы сравнения,
сложения, вычитания и произведения для экземпляров этого класса.
"""
import math


class Drob:
    def __init__(self, ch, zn):
        if zn == 0:
            raise ValueError("Zn cannot be 0!")
        if not (isinstance(ch, int) and isinstance(zn, int)):
            raise ValueError('Zn and ch must be integers')
        self.ch = ch
        self.zn = zn

    def __str__(self):
        self.reduction()

        if self.ch < self.zn:
            return f'correct drob {self.ch}/{self.zn}'
        elif self.ch > self.zn:
            return f'wrong drob {self.ch}/{self.zn}'
        return '1'

    def reduction(self):
        max_d = math.gcd(self.ch, self.zn)

        self.ch = self.ch // max_d
        self.zn = self.zn // max_d

    def __add__(self, other):
        if isinstance(other, Drob):
            new_ch = self.ch * other.zn + self.zn * other.ch
            new_zn = self.zn * other.zn
            return Drob(ch=new_ch, zn=new_zn)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Drob):
            return self.ch / self.zn == other.ch / other.zn
        else:
            return NotImplemented

    def __gt__(self, other):
        return self.ch / self.zn > other.ch / other.zn

    def __ge__(self, other):
        return self.ch / self.zn >= other.ch / other.zn

    def __le__(self, other):
        return self.ch / self.zn <= other.ch / other.zn

    def __lt__(self, other):
        return self.ch / self.zn < other.ch / other.zn

    def __mul__(self, other):
        result1 = self.ch * other.ch
        result2 = self.zn * other.zn
        return Drob(result1, result2)


if __name__ == '__main__':
    d_1 = Drob(2, 3)
    d_2 = Drob(1, 5)

    print(f'd_1 + d_2: {d_1 + d_2}')
    print(f'd_1 > d_2: {d_1 > d_2}')
    print(f'd_1 < d_2: {d_1 < d_2}')
    print(f'd_1 >= d_2: {d_1 >= d_2}')
    print(f'd_1 <= d_2: {d_1 <= d_2}')
    print(f'd_1 == d_2: {d_1 == d_2}')
    print(f'd_1 * d_2: {d_1 * d_2}')
