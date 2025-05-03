# using cls

class Counter:
    count = 0      # Class variable shared by all instances

    def __init__(self):

        # Each time an object is created, increase the class variable 'count'
        Counter.count += 1

    @classmethod
    def counter_display(cls):

        # 'cls' refers to the class itself (not a specific object)
        # Used here to access the class variable 'count'
        return f"Total created objects are: {cls.count}"


# Creating multiple objects of the Counter class
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()
obj6 = Counter()

# Calling the class method using the class name to display the total count
total_objects = Counter.counter_display()
print(total_objects)