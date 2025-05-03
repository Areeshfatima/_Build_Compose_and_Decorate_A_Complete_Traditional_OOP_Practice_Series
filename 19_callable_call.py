# callable() __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number
    
m = Multiplier(6)

# Check if object is callable
print(callable(m))

# Call the object like a function
print(m(4))
