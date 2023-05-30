phone_book: list[dict[str,str]] = []
path = 'phonebook.txt'


def open_file():
    global phone_book
    with open(path, 'r', encoding= 'UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        new = {'name':contact[0], 'phone': contact[1], 'city': contact[2]}
        phone_book.append(new)



def save_file():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(';'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)



def get_book():
    global phone_book
    return phone_book



def add_contact(new: dict[str, str]) -> str:
    global phone_book
    phone_book.append(new)
    return new.get('name')

