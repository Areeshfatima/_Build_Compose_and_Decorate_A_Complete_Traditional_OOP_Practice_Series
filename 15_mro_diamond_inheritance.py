# Method Resolution Order(MRO) and Diamond Inheritance

# Class A with method show()
class A:
    def show(self):
        print("Method from Class A")

# Class B that inherits from A and overrides show()
class B(A):
    def show(self):
        print("Method from Class B")


# Class B that inherits from A and overrides show()
class C(A):
    def show (self):
        print ("Method from Class C")

# Class D that inherits from both B and C
class D(B, C):
    pass

# Create an object of D and call show()
obj = D()
obj.show()   # This will display the output based on MRO



