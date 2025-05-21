# remembering objects

class Song:

    all = []

    def __init__(self, name):
        self.name = name
        #store the entire instance inside the all attribut
        Song.all.append(self)
        #returns a printable version o the class instance
    def __repr__(self):
        return f"(Song <Name:{self.name}>)"
    


Bodak_Yellow = Song("Bodak Yellow")
song2 = Song("Brother Stone")
print(Song.all)



#Example 2
class ShoppingList:
    all = []
    total = 0
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        #store the instance inside the all attribute
        ShoppingList.all.append(self)

    def __repr__(self):
        return f"<ItemName:{self.name}, Price: {self.price}, Quantity: {self.quantity}>"

    @classmethod
    def calculate_total(cls):
        total = 0
        for n in cls.all:
            total += n.price*0.9 * n.quantity
        return total



item1 = ShoppingList(name = "Sugar", price=140, quantity=1)
item2 = ShoppingList(quantity=2, name="Colgate", price=200)
item3 = ShoppingList("Majani Chai", 300,1)
item4 = ShoppingList("Mouse", 500, 2)
print(ShoppingList.all)
print("Total", ShoppingList.calculate_total())



# object relationships


# one to many -> Parent to Child

class Parent:
    def __init__(self, name):
        self.name = name
        #we will use this to store instances of the child class
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Child:
    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f"Child {self.name}"

parent1 =Parent("Jane")
child1 = Child("Tabitha")
child2=Child("Trevor")
#we are able to save child info to the parent class
parent1.add_child(child1)
parent1.add_child(child2)

print(parent1.children)