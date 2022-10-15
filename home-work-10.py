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

    def __repr__(self):
        rep = ", ".join([phone.value for phone in self.phones])

        return rep

    def add_contact(self, phone):
        for phone in self.phones:
            if phone.value == phone:
                raise ValueError("This number is already in your contact list.")
        self.add_contact(phone)

    def replace_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def remove_contact(self, name):
        self.name.pop(name)


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
    split_contact = contact.strip().split()
    name = split_contact[0]
    phone = split_contact[1]
    record_add = Record(name, phone)
    record_add.add_record(record_add)
    new_contact = f'A new contact {name} {phone}, has been added.'
    print(new_contact)
    return new_contact

@input_error
def add_new_phone(contact):
    split_contact = contact.strip().split()
    name = split_contact[0]
    phone = split_contact[1]
    record_add_phone = addressbook.data[name]
    record_add_phone.add_phone(phone)
    return f"A new phone: {phone}, has been added to contact name: {name}."

@input_error
def chandler(name_and_phone):
    split_contact = name_and_phone.strip().split()
    name = split_contact[0]
    phone = split_contact[1]
    new_phone = split_contact[2]
    record_change = addressbook.data[name]
    if record_change.change_phone(old_phone=phone, new_phone=new_phone) is True:
        message = f'A contact name: {name} number: {phone}, has been changed to {new_phone}.'
        print(message)
        return f'A contact name: {name} number: {phone}, has been changed to {new_phone}.'
    else:
        message_2 = 'The phone number not exist'
        print(message_2)
        return 'The phone number not exist'

@input_error
def get_phone(name):
    name = name[0]
    phone = f"'name:' {CONTACTS.data[name].name.value}, 'phone:'{list(map(lambda x: x.value, CONTACTS.data[name].phones))}"
    print(phone)
    return phone

@input_error
def delete_contact(contact):
    split_contact = contact.strip().split()
    name = split_contact[0]
    CONTACTS.pop(name)
    print(f"Contact {name} is deleted")
    return f"Contact {name} is deleted"

@input_error
def show_all():
    string = ', '.join([f'{name} {telephone}' for name, telephone in CONTACTS.items()])
    contacts = repr(string)
    print(contacts)

    return contacts

COMMANDS = {
    "good bye": quit_func,
    "close": quit_func,
    "exit": quit_func,
    "add": add_contact,
    "hello": hello_func,
    "change": chandler,
    "phone": get_phone,
    "show all": show_all,
    "remove": delete_contact,
    "add phone":
}


if __name__ == "__main__":
    main()




