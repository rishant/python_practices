def create_employee_object(name:str, city:str) -> dict:
    emp = {}
    for input in [name, city]:
        if not isinstance(input, str):
            raise TypeError('Please make sure all inputs are strings')

    emp["name"] = name
    emp["city"] = city
    return emp

emp1 = create_employee_object("rishant gupta", "ganganagar (Rajasthan)")
print(emp1)

emp2 = create_employee_object("rammohan", "bangalore (Karnataka)")
print(emp2)

emp3 = create_employee_object(3, 65.3)
print(emp3)
