"""
 Напишите функцию-генератор, которая будет возвращать простые числа.
Верхняя граница этого диапазона должна быть задана параметром этой
функции.
"""


def generator_prime_values(stop: int):
    for num in range(2, stop):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


for v in generator_prime_values(100):
    print(v, end=' ')
