a = 10
b = 10

print(a,b)

# check variable memory address
print(id(a), id(b))

# check variable memory address - After update variable value
b = 20
print(id(a), id(b))

# check variable memory address - After update variable value
a = 20
print(id(a), id(b))