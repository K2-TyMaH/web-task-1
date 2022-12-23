from address_book import address_book


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact doesn't exist, please try again."
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return "Wrong format. Must be '{command} {name} {value}'."
        except TypeError:
            return "Unknown command or parameters, please try again."
        except AttributeError:
            return "Wrong format of date."
        except StopIteration:
            return "There are no other numbers in the book."

    return inner

@input_error
def help_func(*_) -> str:
    options_bot_str = {
    "days to birth 1999.12.23": "кількість днів до твого дня народження", #???? Функція не приймає аргументи, а має
    "add phone Natally 096-45-34-876": "запишу номер телефона твого друга/ подруги",
    "change phone Natally 096-45-34-876": "поміняю номер телефона твого друга/ подруги",
    "del phone Natally 096-45-34-876": "видалю номер телефона твого недруга",
    "show all 3": "покажу весь список контактів",
    "add birth Natally 1999.12.23": "додам день народження твого друга/ подруги, щоб ти не забув привітати",
    "change birth Natally 1999.12.23": "",
    "all births": "",
    "add note Natally str. Peremogy, house 76.": "",
    "change note Natally str. Gagarina, h.126.": "",
    "del note Natally": "",
    "add tag Natally #address #favorite": "",
    "find tag #favorite": "",
    "good bye": "",
    "exit": "",
    "close": "",
    "add Natally 096-45-34-876": "",
    "help": "",
    "sort": "", #??? які аргументи отримує функція
    "find house 76": "",
    "phone Natally": ""
    }

    table_options_bot = ""
    header_table = "| {:<51} | {:<80}".format("Example command", "Command description") # в наст. рядку header_table повертає строку на початку якої ще є текст "\x1b[1m\x1b[34m", тому ширина перщої колонки 25 символів
    header_table = "\033[1m\033[34m{}\033[0m".format(header_table)  
    table_options_bot += f"\n{header_table}\n\n"
    
    for key, value in options_bot_str.items():
        key = "\033[34m{}\033[0m".format(key)
        row = "| {:<60} | {:<80}".format(key, value)
        table_options_bot += f"{row}\n"

    return table_options_bot    

@input_error
def add_func(args: list) -> str:
    pass

@input_error
def add_phone_func(args: list) -> str:
    pass

@input_error
def change_phone_func(args: list) -> str:
    pass

@input_error
def phone_func(args: list) -> str:
    pass

@input_error
def del_phone_func(args: list) -> str:
    pass

@input_error
def show_all_func(*_) -> str:
    pass

@input_error
def add_birth_func(args: list) -> str:
    pass

@input_error
def change_birth_func(args: list) -> str:
    pass

@input_error
def days_to_birth_func(*_) -> str:
    pass

@input_error
def all_birth_func(args: list) -> str:
    pass

@input_error
def add_note_func(args: list) -> str:
    pass

@input_error
def change_note_func(args: list) -> str:
    pass

@input_error
def del_note_func(args: list) -> str:
    pass

@input_error
def add_tag_func(args: list) -> str:
    pass

@input_error
def find_tag_func(args: list) -> str:
    pass

@input_error
def find_func(args) -> str:
    pass

@input_error
def sort_func(args) -> str:
    pass

@input_error
def exit_func(*_)-> str:
    """
    The function close bot.
    """
    return "Good bye!"

#Importantly! The more words in the bot command, the higher they are in the dictionary.
FUNCTIONS = {
    "days to birth": days_to_birth_func,
    "add phone": add_phone_func,
    "change phone": change_phone_func,
    "del phone": del_phone_func,
    "show all": show_all_func,
    "add birth": add_birth_func,
    "change birth": change_birth_func,
    "all births": all_birth_func,
    "add note": add_note_func,
    "change note": change_note_func,
    "del note": del_note_func,
    "add tag": add_tag_func,
    "find tag": find_tag_func,
    "good bye": exit_func,
    "exit": exit_func,
    "close": exit_func,
    "add": add_func,
    "help": help_func,
    "sort": sort_func,
    "find": find_func,
    "phone": phone_func
    }

@input_error
def handler(input_string: str) -> list:
    """
    The function separates the command word for the bot, and writes all other data into a list, where the first value is the name
    """
    command = input_string
    data = ""
    for key in FUNCTIONS:
        if input_string.strip().lower().startswith(key):
            command = key
            data = input_string[len(command):]
            break

    if not input_string.strip().lower().startswith(key):
        raise ValueError("This command is wrong.")

    if data:        
        args = data.strip().split(" ")
        return FUNCTIONS[command](args)
    
    return FUNCTIONS[command]()


def main():
    """
   The user enters through a space:
        - a command for the bot;
        - command, contact name, phone number or date of birth, email address, notes, tags,
    The function returns the bot's response and prints them.
    The bot terminates after the words "good bye" or "close" or "exit"
    """
    try: 
        print("")
        print("\033[1m\033[34m{}\033[0m".format("Hello, I am Bot-contacts:)"))
        print("")
        #print("Type 'help' to see all commands")
        help_str = "\033[34m{}\033[0m".format("help")
        print(f"Type {help_str} to see all commands")
        
        while True:
            print("")
            input_string = input("Input command, please: ")
            get_command = handler(input_string)
            print(get_command)
            if get_command == "Good bye!":
                exit()

    finally:
        address_book.save_address_book()           


if __name__ == '__main__':
    main()    