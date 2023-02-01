
# comments using # symbol

# varable declarations and initialization
data = 1
print(data)
print(type(data))
data = 1.1
print(type(data))
data = 5465786754563209786652476675463523489372076931087597324096840580238460359
print(type(data))
data = 3 + 2j
print(data)
data = complex(3)
print(data)
data = 'a'
print(type(data))
data = 'absdc'
print(type(data))
data = "absdcgdf54364542312"
print(type(data))
data = []
print(type(data))
data = [[]]
print(type(data))
data = True
print(type(data))


# Casting value
print(type(3))
data = str(3)
print(type(data))

data = "Forign Exchange"
print(len(data))
print(data[0], data[len(data)-1])
print(data[2:5])

#tuple ("apple", "banana", "cherry")
fruits = ("apple", "banana", "cherry")
print(type(fruits))

#list ["apple", "banana", "cherry"]
fruits = ["apple", "banana", "cherry"]
# exception for unpack using more value then asking for unpack ==> fruits = ["apple", "banana", "cherry", "mango"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
print(type(fruits))

#Set {"apple", "banana", "cherry"}
fruits = {"apple", "banana", "cherry"}
print(type(fruits))

# dictonry {"f1" : "apple", "f1" : "banana", "f1" : "cherry"}
fruits = {"f1" : "apple", "f1" : "banana", "f1" : "cherry"}
print(type(fruits))

data = type(3)
print(data, 3, data)

x1 = "awesome"

def myfunc1():
  x1 = "fantastic"
  print("Python is " + x1)

myfunc1()
print("Python is " + x1)

def myfunc2():
  global x2
  x2 = "fantastic"

myfunc2()
print("Python is " + x2)