#  using self

class Student:
    def __init__(self, name, marks):   

        # self refers to the current object of the class
        # These instance variables store data unique to each object
        self.name = name
        self.marks = marks

    
    def display(self):

        # Accessing instance variables using self

        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}") 

# Creating an object of Student class with name and marks
student1 = Student("Hoorain", 90)

# Calling the display method to show the student's data
student1.display()

