class OrderIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index = self.index + 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


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

        return f'Цена заказа: {self.calculate_order_price()}\nЗаказ от {str(self.client)}\n\nТовары:\n{products_information}'

    def __iter__(self):
        return OrderIterator(self.products)
