"""
Создайте дескриптор, который будет делать поля класса управляемые им
доступными только для чтения.
"""


class ReadOnlyProperty:
    def __init__(self):
        self.initialized = False

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.initialized:
            raise AttributeError(f"Attempt to modify read-only property '{self.name}'.")

        instance.__dict__[self.name] = value
        self.initialized = True

    def __delete__(self, instance):
        raise AttributeError(f"Attempt to delete read-only property '{self.name}'.")


class Point:
    x = ReadOnlyProperty()
    y = ReadOnlyProperty()

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.x, p.y)

try:
    p.x = 4
except AttributeError as e:
    print(e)
    print(p.x)

try:
    del p.y
except AttributeError as e:
    print(e)
    print(p.y)

