# Class Decorator

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet     # Add method dynamically
    return cls

# Apply the decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Duaa")
print(p.greet())

