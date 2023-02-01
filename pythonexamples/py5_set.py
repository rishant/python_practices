print('"Sets"')
var1 = set([1, 2, 3])
var2 = {2, 3, 4, 5}
print(var1)
print(var2)
print(var1 | var2)
print(var1 & var2)
print(var1 - var2)
# {1, 2, 3}
# {2, 3, 4, 5}
# {1, 2, 3, 4, 5}
# {2, 3}
# {1}

print('"Add/Remove"')
var1.add(4)
print(var1)
var1.remove(4)
print(var1)
# {1, 2, 3, 4}
# {1, 2, 3}

print('"Check if content in set."')
print(2 in var1)
# True
