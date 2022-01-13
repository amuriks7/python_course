
class Customer:
    def __init__(self, name, surname, patronymic, telephone, address):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.telephone = telephone
        self.address = address

    def __str__(self):
        return f"Customer: {self.name} {self.surname} {self.patronymic}\ntelephone: {self.telephone}\naddress: {self.address}"
