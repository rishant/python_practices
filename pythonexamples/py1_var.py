"""
Variable Examples.

This is a docstring that is used a the top of
a file to describe the module.
"""
print('"Assingment and incrementing"')
var = 3
var += 1
print(var)
# 4

print('\n"Multiple assignment"')
var1, var2 = 1, 2
print(var1, var2)

print('\n"Types"')
var = 3 / 2
print(var)
print(type(var))
# 1.5
# <class 'float'>

var = 3 // 2
print(var)
print(type(var))
# 1
# <class 'int'>

print('\n"Changing Types"')
var1 = int(3.2)
var2 = float(3)
print(isinstance(var1, int))
print(isinstance(var2, float))
print(isinstance(var1, (int, float)))
print(isinstance(var2, (int, float)))
# True
# True
# True
# True

print('\n"Variable Scopeing"')
var = 3

def read_only_global():
    print('Read Global: ', var)

def write_read_local():
    # This assignment is local, not global
    var = 2
    print('Local: ', var)

def write_read_global():
    global var
    var = 2
    print('Global: ', var)

read_only_global()
write_read_local()
read_only_global()
write_read_global()
read_only_global()

# Read Global: 3
# Local: 2
# Read Global: 3
# Global: 2
# Read Global: 2
