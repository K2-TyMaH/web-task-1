from collections import UserDict
import pickle
from record import Record


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.load_address_book()

    def add_record(self, record: Record) -> str:
        '''Додає ім'я як ключ та об'єкт класу Рекорд як значення.'''
        self.data[record.name.value] = record
        return f'New contact was added successfuly.'

    def search_in_contact_book(self) -> str:
        '''Шукає співпадіння по цифрі в телефоні, по букві в імені, мейлу.'''
        pass

    def get_all_records(self) -> list:
        '''Повертає список всіх контактів із їхніми даними.'''
        pass

    def all_birthdays(self, range_days) -> list:
        '''Повертає список всіх днів народжень за проміжок днів заданих користувачем.'''
        list_accounts = []
        for record_elem in self.data.values():
            if record_elem.birthday:
                days_to_next_birthday = record_elem.days_to_birthdays()
                if days_to_next_birthday <= range_days:
                    list_accounts.append(record_elem.name.value)
            else:
                continue
        return list_accounts


    def delete_record(self, contact_name: str) -> str:
        '''Видаляє контакт повністю.'''
        self.data.pop(contact_name)
        return f'The contact was deleted successfully.'


    def save_address_book(self) -> str:
        '''Зберігає адресну книгу'''
        with open("address_book.bin", "wb") as file:
            pickle.dump(self.data, file)
    

    def load_address_book(self) -> str:
        '''Завантажує адресну книгу.'''
        try:
            with open("address_book.bin", "rb") as file:     
                self.data = pickle.load(file)
        except FileNotFoundError:
            return "The file does not exist."   
        

    def iterator(self) -> list:
        '''Повертає кількість сторінок, вказаних користувачем.'''
        pass


address_book = AddressBook()
