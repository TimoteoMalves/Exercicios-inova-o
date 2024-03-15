class Compras:
    def __init__(self):
        self.compras = {}

    def add_item(self, name, price):
        self.compras[name] = price

    def show_list(self):
        for key, value in self.compras.items():
            print(f"{key}: {value}\n")

    def remove_item(self, name):
        del self.compras[name]
            
    def calculate_items(self):
        sum = 0
        for value in self.compras.values():
            sum += int(value)

        print (f"Sum: {sum}")
        

def menu():
    print('1 - add\n2 - remove\3 - show\n4 - calcular\n5 - Exit')
    opc = str(input("Option: "))
    return opc

def main():
    list = Compras()

    while True:
        opc = menu()

        if opc == 1:
           item = str(input("Item: "))
           price = str(input("Price: "))
           list.add_item(item, price)

        elif opc == 2:
            list_remove = str(input("Item to be remove: "))
            list.remove_item(list_remove)

        elif opc == 3:
            list.show_list()

        elif opc == 4:
            list.calculate_items()

        elif opc == 5:
            break
        

main()

