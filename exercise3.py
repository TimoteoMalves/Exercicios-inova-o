import json

def add_contact(name, phone, e_address, contacts ):
    contact = {}

    contact["name"] = name
    contact["phone"] = phone
    contact["email"] = e_address
    contacts.append(contact)

    return contacts


def remove_contact(name, contacts):
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

contacts = []


contacts = add_contact("Timoteo", "55981304521", "timoteo.alves@gmail.com", contacts)
contacts = add_contact("Teste", "55981304521", "teste.alves@gmail.com", contacts)
contacts = add_contact("Silva", "55981304521", "silva.alves@gmail.com", contacts)
contacts = remove_contact("Timoteo", contacts)
print(contacts)
search_contact(contacts)
write_file(contacts)




