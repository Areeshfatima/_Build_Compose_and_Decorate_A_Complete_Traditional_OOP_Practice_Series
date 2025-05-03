# Composition

# Engine class
class Engine:
    def start(self):
        return "Engine started."
    
# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine    # Composition: Car "has an" Engine

    def start_car(self):
        return self.engine.start()  # Accessing Engine's method

my_engine = Engine()
my_car = Car(my_engine)

print(my_car.start_car())