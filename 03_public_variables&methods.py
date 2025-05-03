# Public Variables and Methods

class Car:
    def __init__(self, brand):

        # 'brand' is a public variable (no underscore or restriction)
        # It can be accessed and modified directly from outside the class
        self.brand = brand

    def start(self):

        # This is a public method — can be called from anywhere
        print(f"{self.brand} is starting.")


# Creating an object of Car class
my_car = Car("Rolls-Royce")

# Accessing the public variable directly
print(my_car.brand)

# Calling the public method
my_car.start()
