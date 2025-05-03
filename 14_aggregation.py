# Aggregation

# Employee class
class Employee:
    def __init__(self, name):
        self.name = name
    
    def get_details(self):
        return f"Employee: {self.name}"
    

# Department class using aggregation
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee     # Department class using aggregation

    def show_department_details(self):
        return f"Department: {self.department_name} , {self.employee.get_details()}"
    
emp1 = Employee("Abrish")    # Employee exists independently
dept1 = Department("Information Technology" , emp1)   # Department has a reference to Employee

print(dept1.show_department_details())

