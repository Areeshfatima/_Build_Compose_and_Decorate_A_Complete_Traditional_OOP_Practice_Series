# Constructor and Destructors

class Logger:
    def __init__(self):

        # Constructor: called automatically when the object is created
        print("Before: Logger Object Created.")

    def __del__(self):

        # Destructor: called automatically when the object is deleted or goes out of scope
        print("After: Logger Object Destructor.")

# Creating an object of Logger class
log = Logger()

# Deleting the object explicitly to trigger the destructor
del log