# Product Inventory Management
# Product Class
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    # print when an object is passed to functions
    def __str__(self):
        return f"ID: {self.product_id} , Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

# Class for the inventory
class Inventory :
    def __init__(self):
        self.products = []

    # add new product
    def add_product (self, product_id, name, price, quantity):
        new_product = Product(product_id, name, price, quantity)
        self.products.append(new_product)
    
    #Upadate product
    def update_product (self, product_id, name, price, quantity):
        for product in self.products:
            if product.product_id == product_id :
                if name :
                    product.name = name
                if price:
                    product.price = price
                if quantity:
                    product.quantity = quantity
                return print ("Updated!")
        return print ("Can't update the inventory.")
    
    #remove product
    def remove_product (self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove (product)
                return print(f"product with ID: {product_id} is Removed successfully")
        return print("Can't remove this product")
    
    # display inventory
    def display_inventory (self):
        print("Available products in the inventory:")
        for product in self.products:
            print (product)


def main():
    inventory = Inventory()
    # Add products
    inventory.add_product(101, 'T-shirt', 450, 50)
    inventory.add_product(102, 'Jeans', 600, 30)
    # Display products
    inventory.display_inventory()

    # Update products
    inventory.update_product(101, 'blouse', 450, 60)
    inventory.display_inventory()

    # Remove product
    inventory.remove_product (102)
    inventory.display_inventory()

if __name__ == "__main__":
    main()
