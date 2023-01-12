class Item:
"""
Defining class names 'item', the class has a constructor method called `__init__()`.
Constructor method is automatically called when an object if the class is created.
In this instance we are naming the item of clothing and its corrolating price.
"""
    def __init__(self, name,, price):
        self.name = name
        self.price = name



class ShoppingBasket:
"""
The constructor method takes no parameter and it initializes an empty 
list attribute called `items` using  the `self` keyword.
`self` keyword refers to the class (object) being created.
When a new ShoppingBasket object is created the constructor methos is call and the `items` attribute
of the object is set to an empty list.
This class definition can be used to create ShoppingBasket objects that have an empty list of items as an attribute. 
The empty list will be used to store the items that are added to the basket.
"""
    def __init__(self):
        self.items = []

"""
Defining a method within the ShoppingBasket class called "add_item".
Taking one parameter "item" and adds the item to the list of items in the ShoppingBasket.
`self` ketword referes to specific ShoppingBasket object.
`append` method of list to add parameter "item" to list stored in `items` attribute of the object.
"""

    def add_item(self, item):
        self.items.append(item)