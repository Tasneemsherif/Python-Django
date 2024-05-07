''' 1. Add New Item: Prompt the user to enter details such as item name, price, and quantity for a new item. Store this information in the inventory.
2. Update Stock: Allow the user to update the quantity of existing items in the inventory.
3. Generate Sales Report: Calculate the total revenue generated from sales. This should include the total revenue for each item and the overall revenue for all items sold.
4. Popular Items: Identify the top three most popular items based on sales quantity.
5. Exit: Provide an option for the user to exit the program.

Requirements
1. Utilize variables to store item details such as name, price, and quantity.
2. Receive input from the user to add new items and update stock quantities.
3. Implement string formatting to display item details and sales reports.
4. Use string methods to manipulate item names (e.g., convert to uppercase).
5. Perform arithmetic operations to calculate total revenue.
6. Utilize if statements to handle logical operations such as checking for popular items and managing the exit option.
7. Implement while and for loops as necessary for iterating through inventory items and generating reports.
8. Ensure the program handles user input errors gracefully.

'''
class Inventory:
    def __init__(self, name, price, quantity ) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sold_quantity = 5


def add_item (inventory):
    new_item = input("Enter the new item name: ").strip().upper()
    try:
        item_price = float(input("Enter the price in this form 0.0 : "))
        item_quantity = int(input("Enter the quantity: "))
    except ValueError: 
        print ("Invalid, Please enter a NUMERIC value.")
        return

    inventory.append(Inventory(new_item, item_price, item_quantity))
    print (f"Item: {new_item} added successfully")

def update_stock(inventory):
    new_item = input("Enter the Updated item: ").strip().upper()

    for item in inventory:
        if item.name == new_item:
            try:
                new_quantity = int(input("Enter the New quantity: "))
                item.quantity += new_quantity
                print (f"Stock Updated, the item '{new_item}' has '{new_quantity}' now.")
                return
            except ValueError:
                print ("Invalid input, Enter a numeric value.")
                return
    print (f"Item '{new_item}' not found.")

def gen_report (inventory) :
    total_revenue = 0.0
    print("\nSales Report:")
    print(
        "{:<20} {:>10} {:>10} {:>15}".format("Item", "Price", "Sold", "Total Revenue")
    )
    print("-" * 55)

    for item in inventory:
        item_revenue = item.sold_quantity * item.price
        total_revenue += item_revenue
        print(
            "{:<20} {:>10.2f} {:>10} {:>15.2f}".format(
                item.name, item.price, item.sold_quantity, item_revenue
            )
        )

    print("-" * 55)
    print(f"Total Revenue: {total_revenue:.2f}\n")


def get_top_items(inventory):
    sorted_inventory = sorted(inventory, key=lambda x: x.sold_quantity, reverse=True)
    top_items = sorted_inventory[:3]

    print("\nTop 3 Popular Items:")
    print("{:<20} {:>10} {:>15}".format("Item", "Sold", "Total Revenue"))
    print("-" * 45)

    for item in top_items:
        item_revenue = item.sold_quantity * item.price
        print(
            "{:<20} {:>10} {:>15.2f}".format(
                item.name, item.sold_quantity, item_revenue
            )
        )

    print("-" * 45)


def main ():
    inventory = []
    # menu
    while True:
        print(
        """Welcome to the management system
        select an Option
        1. Add New item
        2. Update Stock
        3. Generate Sales Report
        4. Popular Items
        5. Exit """
           )

        option = int(input("Enter the number: "))
        if option == 1:
         add_item(inventory)

        elif option == 2:
          update_stock(inventory)


        elif option == 3:
           gen_report(inventory)
 
        elif option == 4:
          get_top_items(inventory)

        elif option == 5:
           print("See you Soon...")
           break

        else:
          print("Invalid Choice!")


if __name__ == "__main__":
    main ()
