class Basket:
"""
Defining class names 'Basket', the class has a constructor method called `__init__()`.
Constructor method is automatically called when an object if the class is created.
In this instance we are naming the item of clothing and its corrolating price.
"""
    def __init__(self, name, price):
        self.name = {}
        self.price = {"trousers": 55.50, "t-shirt": 25.50, "bandanna": 12.50}


"""
Defining a method within the ShoppingBasket class called "add_item".
Taking one parameter "item" and adds the item to the list of items in the ShoppingBasket.
`self` ketword referes to specific ShoppingBasket object.
`append` method of list to add parameter "item" to list stored in `items` attribute of the object.
"""

    def add_item(self, item, quantity):
        self.items[item] = quantity
    
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"Item {item} not found in basket")