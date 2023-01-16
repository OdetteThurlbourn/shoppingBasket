
"""
Defining class names 'Basket', the class has a constructor method called `__init__()`.
Constructor method is automatically called when an object of the class is created.
In this instance we are naming the item of clothing and its corrolating price.
"""
class Basket:
    def __init__(self, name, price):
        self.name = {}
        self.price = {"trousers": 55.50, "t-shirt": 25.50, "bandanna": 12.50}


"""
Defining a method within the Basket class called "add_item".
Taking one parameter "item" and adds the item to the list of items in the Basket.
`self` ketword referes to specific Basket object.
`append` method of list to add parameter "item" to list stored in `items` attribute of the object.
"""
    def add_item(self, item, quantity):
        self.items[item] = quantity


"""
This function "remove_item" takes a parameter "item". Checks if given "item" is in the "items" list.
If "item" is present, it is removed bu using the "del" statement. 
If "item" is not found it prints the message "Item {item} not found".
"""
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"Item {item} not found in basket")

"""
This function called "view_basket" does not take any parameters. 
It iterates over the items in the basket and thier quantities.  With each iteration it prints
the name and the quantity of the item. If the "items" list is empty, 
it prints a message saying that the basket is empty.
"""
    def view_basket(self):
        if self.items:
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")
        else:
            print("Basket is empty.")


"""
This function does not take in any parameter. 
It checks if the "items" attribute of the object on which this method is called is not empty.
If NOT empty, it iterates over the items and thier quantities in the "items" list.
For each iteration it calculates cost of that item by multiplying the quantity of item by its price.
Keeps adding cost to a variable "total_cost". Then prints item name, quantity and cost. Prints total cost
by printing the value of the "total_cost" variable.
"""
    def checkout(self):
        total_cost = 0
        for item, quantity in self.items.items():
            cost = self.prices[item] * quantity
            total_cost += cost
            print(f"{item}: {quantity} x {self.prices[item]} = {cost}")
        print(f"Total cost: {total_cost}")
    

"""
The function asked the user to confirm the purchase by capturing the input from user using variable named
"confirm".  If user confirms purchase by typing "yes", it clears the item in the "items" list of the object
on which this method is called using the `clear()` method, prints a messages "Purchase confirmaed"
and returns the tptal cost of the purchase. 
If the user does NOT confirm by typing anything other than "yes", it prints a message "Purchase cancelled".
"""
confirm = input("Confirm purchase? (yes/no")
if confirm == "yes":
    self.items.clear()
    print("Purchase confirmed")
    return total_cost
else:
    print("Purchase cancelled.")
