class Product:
    def __init__(self, id, name, description, cost, quantity, margin):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.quantity = quantity
        self.margin = margin
        self.price = 0

    def register_product(self, callback):
        self.price = self.cost / (1 - self.margin)
        callback(self)

    def print_product_list(products):
        for product in products.values():
            print(f"ID: {product.id}")
            print(f"Name: {product.name}")
            print(f"Description: {product.description}")
            print(f"Cost: {product.cost}")
            print(f"Quantity: {product.quantity}")
            print(f"Price: {product.price}")
            print("------------------------------")

    def register_product_from_console():
        id = int(input("ID: "))
        name = input("name: ")
        description = input("description: ")
        cost = float(input("cost: "))
        quantity = int(input("quantity: "))
        margin = float(input("margin: "))

        product = Product(id, name, description, cost, quantity, margin)
        product.register_product(assign_price)

        products[product.id] = product

products = {}

def assign_price(product):
    product.price = product.cost / (1 - product.margin)

Product.register_product_from_console()

Product.print_product_list(products)