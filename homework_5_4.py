# Запит у користувача 
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give an existing name, please"
        except IndexError:
            return "Give an existing phone, please"
    return inner

# додавання нових контактів 
@input_error
def add_contact(args, contacts):
  name, phone = args
  contacts[name] = phone
  return "Contact added."

# Заміна контакта 
@input_error
def change_contact(args, contacts):
    old_name, new_name, new_phone = args
    if old_name in contacts:
        contacts.pop(old_name)
        contacts[new_name] = new_phone
        return "Contact changed."

# показ телефоної книги
@input_error
def show_phone(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# бот виводить у консоль номер телефону для зазначеного контакту
@input_error
def contact_search(name_phone, contacts):
    if name_phone in contacts:
        return f"{name_phone}: {contacts[name_phone]}"
    else:
        return "Contact not found."

# Головна функція 
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_phone(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone": 
                print(contact_search(args[0], contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()