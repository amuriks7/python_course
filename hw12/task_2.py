"""Создайте класс его наследующий."""


from hw12.task_1 import PrimeValue


class Integer(PrimeValue):
    def is_prime(self, num) -> bool:
        for n in range(2, int(num ** 1 / 2) + 1):
            if num % n == 0:
                return False
        return True
