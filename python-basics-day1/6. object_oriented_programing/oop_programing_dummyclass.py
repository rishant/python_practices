class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

emp1.name = "rishant gupta"
emp1.city = "ganganagar (Rajasthan)"

emp2.name = "rammohan"
emp2.city = "bangalore (Karnataka)"


print(emp1, emp2)

print(emp1.__hash__(), emp2.__hash__())