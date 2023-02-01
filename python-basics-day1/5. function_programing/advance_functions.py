# function definition sample
# list
def countFriends11(params):
    print(params)
    print(type(params))
    print("print index 0 value: ", params[0])
    print(len(params))

countFriends11(["op","num2","num1"])

# function definition sample
# tuple
def countFriends21(params):
    print(params)
    print(type(params))
    print("print index 0 value: ", params[0])
    return len(params)

print(countFriends21((1, 2)))

# tuple
def countFriends22(*params):
    print(params)
    print(type(params))
    print("print index 0 value: ", params[0])
    return len(params)

print(countFriends22(1, 2, 3))
 
# dict
def countFriends31(params):
    print(params)
    print(type(params))
    print(params["op"])

countFriends31({"op":"+", "num2":1, "num1":2})

# dict
def countFriends32(**params):
    print(params)
    print(type(params))
    print(params["op"])

countFriends32(op="+", num2=1, num1=2)