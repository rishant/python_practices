class Employee:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def printEmployeeDetails(self):
        print("Employee Name: " + self.name + ", Employee City: " + self.city)

    @classmethod
    def classChangeMe(cls):
        print("class")

    @staticmethod
    def staticChangeMe(cls):
        print("static")

emp1 = Employee("rishant gupta", "ganganagar (Rajasthan)")
emp2 = Employee("rammohan", "bangalore (Karnataka)")

print(emp1, emp2)
print(emp1.__hash__(), emp2.__hash__())
emp1.printEmployeeDetails()
emp2.printEmployeeDetails()