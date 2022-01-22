"""
Создайте декоратор с параметрами для проведения хронометража работы
той или иной функции. Параметрами должны выступать то, сколько раз нужно
запустить декорируемую функцию и в какой файл сохранить результаты
хронометража. Цель - провести хронометраж декорируемой функции.
"""
import functools
import timeit


def write_to_txt_file(filename: str, content: str) -> None:
    with open(f'{filename}.txt', 'w') as file:
        file.write(content)


def func_timing(times=1, filename='timing'):
    def _inner(f):
        def __inner(*args, **kwargs):
            result = timeit.Timer(functools.partial(f, *args, **kwargs)).timeit(times)
            print(result)
            write_to_txt_file(filename, f'{result} seconds')

            return f(*args, **kwargs)
        return __inner
    return _inner


@func_timing(55)
def func():
    return [x**2 for x in range(10000)]


func()
