print('"Dictionary"')
d1 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

print(d1)
print(d1["a"])
try:
    d1["e"]
except KeyError:
    print("Key not found!")
print(d1.get("e"))
print(d1.get("e", "some default"))
# {'b': 2, 'a': 1, 'c': 3, 'd': 4}
# 1
# Key not found!
# None
# some default

print('\n"Add/Remove/Modify"')
d1["e"] = 5
print(d1["e"])
del d1["d"]
try:
    d1["d"]
except KeyError:
    print("Key not found!")
d1["a"] = 0
print(d1["a"])
# 5
# Key not found!
# 0

print('\n"Get all keys/values"')
keys = sorted(d1.keys())
values = sorted(d1.values())
print(keys)
print(values)
keys = []
values = []
for k, v in d1.items():
    keys.append(k)
    values.append(v)
print(sorted(keys))
print(sorted(values))
# ['a', 'b', 'c', 'e']
# [0, 2, 3, 5]
# ['a', 'b', 'c', 'e']
# [0, 2, 3, 5]

print('\n"Any hashable object can be a key"')
d2 = {
    1: "a",
    2: "b",
    3: "c",
    (1, 2, 3): "d"
}
print(d2)
# {1: 'a', 2: 'b', 3: 'c', (1, 2, 3): 'd'}
