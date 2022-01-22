"""
Предположим, в классе определен метод __str__, который возвращает
строку на основании класса. Создайте такой декоратор для этого метода,
чтобы полученная строка сохранялась в текстовый файл, имя которого
совпадает с именем класса, метод которого вы декорировали.
"""


def write_to_txt_file(filename: str, content: str) -> None:
    with open(f'{filename}.txt', 'w') as f:
        f.write(content)


def write_str_of_class_to_file(f):
    def _inner(*args, **kwargs):
        classname = args[0].__class__.__name__
        result = f(*args, **kwargs)
        write_to_txt_file(classname, result)

        return result

    return _inner


class Car:
    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year

    @write_str_of_class_to_file
    def __str__(self):
        return f'{self.model} {self.year}'


class Human:
    def __init__(self, age: int):
        self.age = age

    @write_str_of_class_to_file
    def __str__(self):
        return f'Human {self.age} years old'


car = Car('BMW', 2020)
print(car)

human = Human(22)
print(human)
