from collections import UserDict
from address_book.Models import Name, Phone, Record


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()  # Это создаст self.data как пустой словарь

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
