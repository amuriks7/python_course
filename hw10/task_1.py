"""
Создайте декоратор, который зарегистрирует декорируемый класс в
списке классов.
"""
class_list = []


def registrator(cls):
    class_list.append(cls)
    return cls


@registrator
class Car:
    pass


@registrator
class Human:
    pass


print(class_list)
