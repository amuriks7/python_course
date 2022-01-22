"""
Для класса Box напишите статический метод, который будет подсчитывать
суммарный объем двух ящиков, которые будут его параметрами.
"""


class Case:
    def __init__(self, width: float, height: float, long: float):
        self.width = width
        self.height = height
        self.long = long

    def calculate_volume(self):
        return self.width * self.height * self.long


class Box:
    @staticmethod
    def total_volume(case1: Case, case2: Case):
        return case1.calculate_volume() + case2.calculate_volume()


case1 = Case(1.1, 0.3, 1.3)
case2 = Case(1.2, 0.2, 1.4)

print(Box.total_volume(case1, case2))
