from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []

    def add_contact(self, phone):
        self.phones.append(Phone(phone))

    def replace_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def remove_contacts(self, phone):
        self.phones.pop(phone)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


CONTACTS = AddressBook()


def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except KeyError:
            print("Enter user name")
            return "Enter user name"
        except ValueError:
            print("Give me name and phone please")
            return "Give me name and phone please"
        except IndexError:
            print("Give me name and phone please")
            return "Give me name and phone please"
        except TypeError:
            print("Wrong command. Try again")
            return "Wrong command. Try again"

    return wrapper
@input_error
def main():
    while True:
        user_input = input('Enter command: ')
        answer = run_command(user_input.strip())
        #print(answer)
        if answer == 'Good bye!':
            break

@input_error
def run_command(user_command):
    command = user_command
    params = ''
    for key in COMMANDS:
        if user_command.lower().startswith(key):
            command = key
            params = user_command[len(command):]
            break
    if params:
        return get_answer_function(command)(params)
    else:
        return get_answer_function(command)()

def get_answer_function(answer):
    return COMMANDS.get(answer, command_error)

@input_error
def command_error():
    return "Wrong command. Try again"

@input_error
def hello_func():
    print("How can I help you?")
    return "How can I help you?"

@input_error
def quit_func():
    print("Good bye!")
    return quit()

@input_error
def add_contact(contact):
    split_contct = contact.strip().split()
    name = split_contct[0]
    phone = split_contct[1]
    CONTACTS.update({"name": "phone"})
    print("New contact added.")
    return "New contact added."

@input_error
def chandler(name_and_phone):
    name, phone = create_data(data)
    new_phone = data[2]

    record_change = addressbook.data[name]
    if record_change.change_phone(old_phone=phone, new_phone=new_phone) is True:
        return f'A contact name: {name} number: {phone}, has been changed to {new_phone}.'
    else:
        return 'The phone number not exist'

@input_error
def get_phone(name):
    name = name[0]
    phone = f"'name:' {CONTACTS.data[name].name.value}, 'phone:'{list(map(lambda x: x.value, CONTACTS.data[name].phones))}"
    print(phone)
    return phone

@input_error
def show_all():
    contacts = '\n'.join([f'{name} {telephone}' for name, telephone in CONTACTS.items()])

    return print(contacts)

COMMANDS = {
    "good bye": quit_func,
    "close": quit_func,
    "exit": quit_func,
    "add": add_contact,
    "hello": hello_func,
    "change": chandler,
    "phone": get_phone,
    "show all": show_all
}


if __name__ == "__main__":
    main()




