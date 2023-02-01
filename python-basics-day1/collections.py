#list => Ordered & Mutable list
list1 = ["op", "num2", "num1"]
print(list1)
list1[0] = 5
print(list1)

#tuple => Ordered & Imutable list
tuple1 = ("op", "num2", "num1")
print(tuple1)
##TypeError: 'tuple' object does not support item assignment
#tuple1[0] = 5 
#print(tuple1)

#set => Unordered & Mutable list
##TypeError: set expected at most 1 argument, got 4 
#set1 = set("op", "num2", "num1", "op")
set1 = {1, "oppo", 1}
print(set1)

set1.add(5)
print(set1)

set1 = set("oppo")
print(set1)

#dictonry
#dict1 = dict({"foo": "bar"})
dict1 = {"foo":"bar", "mono":"lithic"}
print(dict1)
print(dict1.keys())
print(dict1.values())

for key, value in dict1.items():
    print(f"Key: {key} value: {value}")

for key in dict1:
    print(f"Key: {key} value: {dict1[key]}")
    