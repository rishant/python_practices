name = "Rishant Gupta"
city = "Sriganganagar (Rajasthan)"

message1 = "Name: " + name + ", City: " + city
print(message1)

message1 = "Name: %s, City: %s" %(name, city)
print(message1)

message1 = "Name: {0}, City: {1}".format(name, city)
print(message1)


message1 = """
    Name: {0}, 

        City: {1}"""
print(message1.format(name, city))

message1 = """
    Simple:
        Name: {}, 
        City: {}
"""
print(message1.format(name, city))

# Exception
# message1 = """
#     Simple:
#         Name: {name}, 
#         City: {city}
# """
# print(message1.format(city, name))