"""
Создайте декоратор, который будет подсчитывать, сколько раз была
вызвана декорируемая функция.
"""


def calls_counter(f):
    def _inner(*args, **kwargs):
        _inner.calls += 1
        return f(*args, **kwargs)

    _inner.calls = 0
    return _inner


@calls_counter
def func(a, b, c='qwe'):
    print(f'{a} << {b} >> {c}')


print(func.calls)
func(1, 3)
func(4, 2, c='qw')
func(5, 3)
func(4, 1, 123)
print(func.calls)
