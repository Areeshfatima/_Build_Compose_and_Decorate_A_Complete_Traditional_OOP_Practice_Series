# Access Modifiers: Public, Private and Protected

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def get_ssn(self):      # read private data safely
        return self.__ssn
    
    def set_salary(self, new_salary):  # set variable to protected variable
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be positive in numbers.")

    def display(self):
        print(f"Name: {self.name}")  # public
        print(f"Salary: {self._salary}")  # protected
        print(f"SSN: {self.__ssn}")  # private

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Accessing SSN via getter command: {self.get_ssn()}")  # private variable

manager1 = Manager("Eshal", "100,000", "696-423-2024", "Information Technology")
manager1.show_manager_info()
manager1.set_salary(200000)
print("Increamented Salary:", manager1._salary)

# print(manager1.__ssn)
print("Private SSN via managed:", manager1._Employee__ssn)



    


