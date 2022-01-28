"""
Создайте ABC класс с абстрактным методом проверки целого числа на
простоту. Т.е., если параметром этого метода является целое число и оно
простое, то метод должен вернуть True, а в противном случае False.
"""

import abc


class PrimeValue(abc.ABC):
    @abc.abstractmethod
    def is_prime(self, num) -> bool:
        pass
