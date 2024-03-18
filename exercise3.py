import json

def add_contact(contacts):
    contact = {}
    name = str(input("Name: "))
    phone = str(input("Phone: "))
    e_address = str(input("e_address: "))


    contact["name"] = name
    contact["phone"] = phone
    contact["email"] = e_address
    contacts.append(contact)

    return contacts


def remove_contact(contacts):

    name = str(input("Name to be removed: "))

    for item in contacts:
        if item['name'] == name: 
            contacts.remove(item)
            return contacts
        else:
            print("not here")

def search_contact(contacts):
    name = str(input("Search: "))
    for item in contacts:
        if item['name'] == name: 
            print(item)
            return
        else:
            print("No contact found")

def show_list(contacts):
    print(contacts)

def write_file(contacts):
    with open("file.json", "w") as f:
        json.dump(contacts, f)
        

def menu():
    print("1 - Add\n2 - Remove\n3 - Search\n4 - Show")
    while True:
        try: 
            opt = int(input('Option: '))
            return opt

        except ValueError:
            print("Not a valid option")


def main():
    contacts = []

    while True:

        opt = menu()

        if opt == 1: 
            contacts = add_contact(contacts)
            write_file(contacts)
            print(contacts)

        elif opt == 2:
            contacts = remove_contact(contacts)
            write_file(contacts)
            print(contacts)

        elif opt == 3:
            search_contact(contacts)

        elif opt == 4:
            print(contacts)

        elif opt == 5:
            break

main()