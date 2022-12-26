from collections import UserDict
import pickle
from record import Record
from datetime import datetime

from print_table import header_func, line_func


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.load_address_book()    
    
    def add_record(self, record: Record) -> str:
        '''Додає ім'я як ключ та об'єкт класу Рекорд як значення.'''
        self.data[record.name.value] = record                 #.title()
        return f'New contact was added successfuly.'

    def search_in_contact_book(self, data) -> str:
        '''Шукає співпадіння по цифрі в телефоні, по букві в імені, мейлу.'''
        
        table = header_func()
        data = data[0] if data else ""
        counter = 0        

        for name, record in self.data.items():

            phones = [phone.value for phone in record.phones]
            phones = " ".join(phones)
            emails = [email.value for email in record.emails]
            emails = " ".join(emails)
            birthday = record.birthday.value.strftime("%m.%d.%Y") if record.birthday else ""
            tag = " ".join(record.tag.value if record.tag else "")
            note = record.note.value if record.note else ""

            if (
                data in name or
                data in birthday or
                data in emails or
                data in phones or
                data in tag or
                data in note
                ):

                table += line_func(record)
                counter += 1 
        
        if counter < 1:
            raise ValueError(f"I didn't find any {data} in AB.")              
        
        return table

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
                    current_year = datetime.now().year
                    current_day = datetime.now()
                    this_year_birthday = datetime(year=current_year, month=record_elem.birthday.value.month, day=record_elem.birthday.value.day)
                    if (this_year_birthday - current_day).days >= 0:
                        next_birth = this_year_birthday - current_day
                        return next_birth.days
                    else:
                        next_birth = datetime(year=current_year + 1, month=record_elem.birthday.value.month, day=record_elem.birthday.value.day)
                    data = [record_elem.name.value.title(), next_birth.strftime("%A %d %B %Y")]
                    list_accounts.append(data)
            else:
                continue
        return list_accounts


    def delete_record(self, contact_name: str) -> str:
        '''Видаляє контакт повністю.'''
        self.data.pop(contact_name)
        return f"The contact '{contact_name.title()}' was deleted successfully."


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


address_book = AddressBook()
