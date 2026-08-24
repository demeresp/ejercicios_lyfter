class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


class Inventory():
    def __init__(self):
        self.products = []


    def add_product(self, object):
        self.products.append(object)


    def show_invetory(self, products):
        for p in products:
            print("Availables products;", products)


    def inventorys_total(self):
        total = 0
        for product in self.products:
            total += product.price * product.amount
        return total


item1 = Product("Coffee", 400, 10)
item2 = Product("Legos", 200, 5)

inventory = Inventory()
inventory.add_product(item1)
inventory.add_product(item2)
print("Total inventory value:", inventory.inventorys_total())

