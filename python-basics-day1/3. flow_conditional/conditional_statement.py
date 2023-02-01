num = 5
if num>0:
    print("Number is positive")
    print("_________End of the execution_________")
print("Bye Bye")

num = -5
if num>0:
    print("Number is positive")
    print("_________End of the execution_________")
else:
    print("Number is netive")
    print("_________End of the execution_________")
print("Bye Bye")

num = 0
if num>0:
    print("Number is positive")
    print("_________End of the execution_________")
elif num<0:
    print("Number is netive")
    print("_________End of the execution_________")
else:
    print("Number is zero")
    print("_________End of the execution_________")
print("Bye Bye")


if num%2==0 and num>0:
    print("Number is positive and even")
elif num%2==0 and num<0:
    print("Number is negative and even")
elif num%2!=0 and num<0:
    print("Number is negative and old")
else:
    print("The number is zero")

for i in range(1,10):
    print(i)

print("\n")

for i in range(1,10,2):
    print(i)

print("\n")

for i in "Hello World":
    print(i)