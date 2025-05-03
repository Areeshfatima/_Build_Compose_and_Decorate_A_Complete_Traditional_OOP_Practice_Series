# Static Variables and Static Method

class MathUtils:
    @staticmethod
    def add(a, b):
        # Static method: does not need self or cls
        # It performs a task related to the class, but doesn't depend on object or class variables
        return a + b
    
# Calling the static method directly using the class name
total = MathUtils.add(6, 9)

# Displaying the result
print(f"Sum of my 2 numbers are: {total}")



