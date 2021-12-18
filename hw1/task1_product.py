"""Создайте пользовательский класс для описания товара
(предположим, это задел для интернет-магазина). В качестве
полей товара можете использовать значение цены, описание,
габариты товара. Создайте пару экземпляров вашего класса и
протестируйте их работу."""


class Book:
    def __init__(self, name, price, pages, year_of_release):
        self.name = name
        self.price = price
        self.pages = pages
        self.year_of_release = year_of_release

    def __str__(self):
        return f"{self.name} price: {self.price} pages: {self.pages} year_of_release: {self.year_of_release}"


if __name__ == "__main__":
    book1 = Book("Python 1 edition", 250, "650", "2011")
    book2 = Book("Python PRO edition", 250, "650", "2011")

    print(book1)
    print(book1.name)

    print(book2)
