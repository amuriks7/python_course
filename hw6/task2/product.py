class Book:
    def __init__(self, name, price, pages, year_of_release):
        self.name = name
        self.price = price
        self.pages = pages
        self.year_of_release = year_of_release

    def __str__(self):
        return f"{self.name} price: {self.price} pages: {self.pages} year_of_release: {self.year_of_release}"
