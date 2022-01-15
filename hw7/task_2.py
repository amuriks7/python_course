"""
Реализуйте свой аналог генераторной функции range(). Да, вы теперь
знаете, что это - генератор.
"""


def my_range(start: int = 0, stop: int = None, step: int = 1):
    if stop is None:
        stop = start
        start = 0

    while start < stop:
        yield start
        start += step


for i in my_range(20):
    print(i)
