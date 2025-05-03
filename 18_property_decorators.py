# Property Decorators: @property, @setter, and @deleter

class Product:
    # Constructor to initialize the price of the product
    def __init__(self, price):
        self._price = price     # private attribute(_price is conventionally considered private)

    # Property decorator to get the price
    @property
    def price(self):
        return self._price
    
    # Setter decorator to set a new price, with validation
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Invalid price! Must be positive in numbers.")
    
    # Deleter decorator to delete the price attribute
    @price.deleter
    def price(self):
        print("Price deleted!")
        del self._price

p1 = Product(1000)
print(p1.price)    # Accessing the price using the @property method

 
p1.price = 2000
print(p1.price)    # Accessing the updated price

del p1.price      # Deleting the price using the deleter method

