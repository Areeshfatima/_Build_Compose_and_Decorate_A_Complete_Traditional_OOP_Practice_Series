# Instance Methods

class Dog:
    def __init__(self, name, breed):
        # Instance variables (every object has different data)
        self.name = name
        self.breed = breed

    def bark(self):
        # Instance method – it works with the object’s own data using 'self'
        print(f"{self.name} says: Woof Woof!")

# Creating an object of Dog
dog = Dog("Max", "German Shepherd")

# Calling the instance method using the object
dog.bark()