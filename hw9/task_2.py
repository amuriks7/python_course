"""
Создайте декоратор, который зарегистрирует декорируемую функцию в
списке функций, для обработки последовательности.
"""

func_list = []


def add_function(f):
    func_list.append(f)
    return f


@add_function
def f1(x, y):
    return x + y


@add_function
def f2(x, y):
    return x - y


@add_function
def f3(x, y):
    return x * y


for func in func_list:
    print(func(4, 5))
