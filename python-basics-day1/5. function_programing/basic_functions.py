# Python code execute from top to bottom, So method call before defunation not allowed
# printEvenOdd(7)

# function definition sample
def printEvenOdd(num: int):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
printEvenOdd(7)

# function definition sample
def printEvenOdd1(num: int):
    if num%2==0:
        return True
    else:
        return False
print(printEvenOdd(7))

# function definition sample
# list
def countFriends1(params):
    print(params)
    print(type(params))
    print("print index 0 value: ", params[0])
countFriends1([1,2,3])

# function definition sample
# tuple
def countFriends2(params):
    print(params)
    print(type(params))
    print("print index 0 value: ", params[0])
    return len(params)
print(countFriends2((1, 2)))

# function definition sample 
# dict
def countFriends3(params):
    print(params)
    print(type(params))
    print(params["op"])
countFriends3({"op":"+", "num2":1, "num1":2})