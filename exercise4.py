import csv
    
def menu():
    print("1 - Add produto\n2 - Atualizar preco\n3 - Remover produto\n4 - Sair")
    opc = int(input("Option: "))
    return opc

def add_product(products):
    product = {}
    produto = str(input("Produto: "))
    price = str(input("Price: "))
    quantidade = str(input("Quantidade: "))

    product["produto"] = produto
    product["price"] = price
    product["quantidade"] = quantidade
    products.append(product)
    return products

def att_price(products):
    product = str(input("Product to be updated: "))
    new_price = int(input("New price: "))
    print(products)
    for item in products:
        if item['produto'] == product: 
            item['price'] = new_price
            return products
        else:
            print("No product found")
    
def remove_product(products):
    product = str(input("Product to be removed: "))

    for item in products:
            if item['produto'] == product: 
                products.remove(item)
                return products
            else:
                print("No product found")


def create_csv(csv_file):
    with open(csv_file, "w", newline="") as arquivo:
        writer_csv = csv.writer(arquivo)
        writer_csv.writerow(["nome", "preco", "quantidade"])

def add_in_csv(csv_file, products):
    for product in products:
        with open(csv_file, "a", newline="") as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow([product["produto"], product["price"], product["quantidade"]])

def main():
    products = []
    csv_file = "example.csv"

    while True:
        opc = menu()
        print(opc)

        if opc == 1:
            products = add_product(products)
            print(products)
            create_csv(csv_file)
            add_in_csv(csv_file, products)

        elif opc == 2: 
            products = att_price(products)
            print(products)
            create_csv(csv_file)
            add_in_csv(csv_file, products)

        elif opc == 3: 
            products = remove_product(products)
            print(products)
            create_csv(csv_file)
            add_in_csv(csv_file, products)

        elif opc == 4:
            break

    return 0 



main()





