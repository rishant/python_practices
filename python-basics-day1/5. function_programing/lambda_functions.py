def square(num: int):
    return num*num
print(square(8))

square1 = lambda x: x*x
print(square1(8))

# Lambda function with if-else
square1 = lambda x : x*x if(x > 0) else None
print(square1(8))

def printEvenOdd(num: int):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

printEvenOdd(7)
printEvenOdd(8)

printEvenOdd1 = lambda num: print("Even") if(num%2==0) else print("Odd")
printEvenOdd1(7)
printEvenOdd1(8)