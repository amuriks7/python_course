"""
Используя функцию замыкания реализуйте такой прием программирования
как Мемоизация - https://en.wikipedia.org/wiki/Memoization
Используйте полученный механизм для ускорения функции рекурсивного
вычисления n — го члена ряда Фибоначчи. Сравните скорость выполнения с
просто рекурсивным подходом.
"""
import time


def fibonacci_1(n):
    current = 1
    if n > 3:
        current = fibonacci_1(n - 1) + fibonacci_1(n - 2)
    return current


def fibonacci_2(n):
    cache = {0: 0, 1: 1}

    def fib(n):
        if n in cache:
            return cache[n]
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib(n)


def fibonacci_3(n):
    fib1, fib2 = 0, 1
    for __ in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


start_time_1 = time.time()
print(f"{fibonacci_1(40)} --- {time.time() - start_time_1} seconds ---")

start_time_2 = time.time()
print(f"{fibonacci_2(39)} --- {time.time() - start_time_2} seconds ---")

start_time_3 = time.time()
print(f"{list(fibonacci_3(40))[-1]} --- {time.time() - start_time_3} seconds ---")
