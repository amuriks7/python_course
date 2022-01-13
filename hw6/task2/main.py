"""
Модифицируете класс Заказ (задание Лекции 1) добавив реализацию
протокола последовательностей и итерационного протокола.
"""


from hw6.task2.customer import Customer
from hw6.task2.order import Order
from hw6.task2.product import Book

if __name__ == "__main__":
    book1 = Book("Python 1 edition", 250, "650", "2011")
    book2 = Book("Python 2 edition", 200, "350", "2020")

    customer = Customer("Andrii", "Muzyka", "Vitaliyvuch", "380677396514", "60071 Bocharova 1, apartament 3")

    order = Order(customer)
    order.add_to_cart(book1)
    order.add_to_cart(book2)

    for product in order:
        print(product)
