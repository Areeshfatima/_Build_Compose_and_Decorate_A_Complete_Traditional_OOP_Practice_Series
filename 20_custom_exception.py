# Creating a Custom Exception


class InvalidAgeError(Exception):
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Age is valid.")

# Use try, except to handle it

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)