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
        current = fibonacci_1(n-1) + fibonacci_1(n-2)
    return current


def fibonacci_2(n):
    fib1, fib2 = 0, 1
    for __ in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


start_time_1 = time.time()
print(f"{fibonacci_1(40)} --- {time.time() - start_time_1} seconds ---")

start_time_2 = time.time()
print(f"{list(fibonacci_2(40))[-1]} --- {time.time() - start_time_2} seconds ---")
