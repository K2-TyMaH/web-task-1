from collections import UserDict


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.load_address_book()

    def add_record(self) -> str:
        '''Додає ім'я як ключ та об'єкт класу Рекорд як значення.'''
        pass

    def search_by_name(self) -> str:
        '''Шукає телефон по імені.'''
        pass

    def search_in_contact_book(self) -> str:
        '''Шукає співпадіння по цифрі в телефоні, по букві в імені, мейлу.'''
        pass

    def get_all_records(self) -> list:
        '''Повертає список всіх контактів із їхніми даними.'''
        pass

    def all_birthdays(self) -> list:
        '''Повертає список всіх днів народжень за проміжок днів заданих користувачем.'''
        pass

    def delete_record(self) -> str:
        '''Видаляє контакт повністю.'''
        pass

    def save_address_book(self) -> str:
        '''Зберігає адресну книгу'''
        pass

    def load_address_book(self) -> str:
        '''Завантажує адресну книгу.'''
        pass

    def iterator(self) -> list:
        '''Повертає кількість сторінок, вказаних користувачем.'''
        pass

address_book = AddressBook()    