# The Super() Function

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with the name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        # super() calls the constructor of the parent class (Person)
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")

# Creating a Teacher object
teacher1 = Teacher("Arsh fatima", "Mathematics")