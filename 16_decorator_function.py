# Decorator Function

def log_function_call(func):
    def wrapper():
        print("Function is being called.")
        return func()
    return wrapper

# Function to decorate
@log_function_call
def say_hello():
    print("Hello, Python!")

say_hello()   # Call the decorated function



