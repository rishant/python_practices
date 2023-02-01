print('"Lists are mutable and variables are references."')
var0 = [1, 2, 3, 4, 5]
var1 = var0
print(var0)
print(var1)
var0[0] = 0
print(var0)
print(var1)
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [0, 2, 3, 4, 5]
# [0, 2, 3, 4, 5]

print('\n"Slicing creates a copy of a list."')
var0 = [1, 2, 3, 4, 5]
var2 = var0[2:]
var3 = var0[:3]
var4 = var0[1:3]
print(var2)
print(var3)
print(var4)
var0[2] = 0
print(var0)
print(var2)
# [3, 4, 5]
# [1, 2, 3]
# [2, 3]
# [1, 2, 0, 4, 5]
# [3, 4, 5]

print('\n"Tuples are immutable."')
t0 = (1, 2, 3)
print(t0)
print(t0[0])
try:
    t0[0] = 1
except TypeError:
    print("Tuples are immutable!")
# (1, 2, 3)
# 1
# Tuples are immutable!

print('\n"Tuples can be sliced."')
print(t0[1:])
# (2, 3)
