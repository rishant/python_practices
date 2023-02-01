print('"Demonstrating arguments."')
def function(num1, num2, add_nums=True, reverse_logic=False):
    """
    Docstring:

    This function does stuff.
    """
    if add_nums and not reverse_logic:
        return num1 + num2
    else:
        return num1 - num2

print(function(3, 2, True))
print(function(3, 2, False))
print(function(3, 2, reverse_logic=True, add_nums=True))
# 5
# 1
# 1

print('\n"Help"')
help(function)
# Help on function function in module __main__:
#
# function(num1, num2, add_nums=True, reverse_logic=False)
#     Docstring:
#
#     This function does stuff.

print('\n"Demonstrate multiple returns."')
def function2():
    return 1, 2

var = function2()
print(var[0])
print(var[1])

var1, var2 = function2()
print(var1)
print(var2)
