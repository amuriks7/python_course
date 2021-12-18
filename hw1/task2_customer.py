"""Создайте класс «Покупатель». В качестве полей можете
использовать фамилию, имя, отчество, мобильный телефон."""


class Customer:
    def __init__(self, name, surname, patronymic, telephone, address):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.telephone = telephone
        self.address = address

    def __str__(self):
        return f"Customer: {self.name} {self.surname} {self.patronymic}\ntelephone: {self.telephone}\naddress: {self.address}"


if __name__ == "__main__":
    client = Customer("Andrii", "Muzyka", "Vitaliyvuch", "380677396514", "60071 Bocharova 1, apartament 3")
    print(client)
