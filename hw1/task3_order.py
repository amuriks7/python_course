"""Создайте класс «Заказ». Заказ может содержать несколько
товаров. Заказ должен содержать данные о пользователе, который
его осуществил. Реализуйте метод вычисления суммарной
стоимости заказа. Определите метод __str__() для корректного
вывода информации о этом заказе."""
from hw1.task1_product import Book
from hw1.task2_customer import Customer


class Order:
    def __init__(self, customer):
        self.client = customer
        self.products = []
        self.order_price = 0

    def add_to_cart(self, product):
        self.products.append(product)
        self.order_price += product.price

    def calculate_order_price(self):
        count = 0

        for product in self.products:
            count += product.price
        return count

    def __str__(self):
        products_information = ''
        for product in self.products:
            products_information += f'\t{str(product)}\n'

        return f'Цена заказа: {order.calculate_order_price()}\nЗаказ от {str(self.client)}\n\nТовары:\n{products_information}'


if __name__ == "__main__":
    book1 = Book("Python 1 edition", 250, "650", "2011")
    book2 = Book("Python 2 edition", 200, "350", "2020")

    customer = Customer("Andrii", "Muzyka", "Vitaliyvuch", "380677396514", "60071 Bocharova 1, apartament 3")

    order = Order(customer)
    order.add_to_cart(book1)
    order.add_to_cart(book2)

    print(order)
