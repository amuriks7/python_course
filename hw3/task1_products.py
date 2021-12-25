"""
Напишите программу, которая реализует функциональность считывания
с клавиатуры стоимости товара. При этом стоит учесть, что пользователь
может ввести не цифры, а смесь цифр и букв или отрицательное число. При
необходимости создайте пользовательское исключение и обработайте его
(например, для отрицательных чисел).
"""


class Book:
    def __init__(self, name, price, pages, year_of_release):
        self.name = name
        self.price = price
        self.pages = pages
        self.year_of_release = year_of_release

    def __str__(self):
        return f"{self.name} price: {self.price} pages: {self.pages} year_of_release: {self.year_of_release}"


if __name__ == "__main__":
    try:
        price = float(input('Цена товара: '))
        if price < 0:
            raise Exception("Invalid price, should be > 0")
    except Exception as err:
        print(err)
    else:
        book1 = Book("Python 1 edition", price, "650", "2011")
        book2 = Book("Python PRO edition", price, "650", "2011")

        print(book1)
        print(book2)
