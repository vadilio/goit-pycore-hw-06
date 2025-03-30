# ---
from parse import parse_input
from proces_data import add_contact, change_contact, get_name_byphone, get_all


def main():
    contacts = []
    error_message = """
Невірна команда:
Введіть: 
Hello - Привитання,
Exit or close - Для виходу,
All - Отримати список контактів,
Add Name Phone - Додати контакт,
Change Username Phone - зміна контакту
Phone Username - Показати контакт
                    """
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print(error_message)
            continue
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_name_byphone(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print(error_message)


if __name__ == "__main__":
    main()
