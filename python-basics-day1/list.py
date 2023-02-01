fruites = ["Apple", 'Guava', 'Papaya']
print(fruites)

fruites[1] = "Mango"
print(fruites)

print(fruites[-1])

# sort in descending order
fruites.reverse()
print(fruites)

# sort in assending order
fruites.sort()
print(fruites)

#IndexError: list assignment index out of range
#fruites[3] = 4
#print(fruites)

# Alternative for IndexError: list assignment index out of range
fruites.append(4)
print(fruites)

fruites.insert(1, 3.14)
print(fruites)

print(fruites.pop(0))
print(fruites.pop(0))
print(fruites)

fruites.clear()
print(fruites)

#del fruites
#print(fruites)

# list comprehension
#new_list = [expression for_item_in_list if_condition]
num = [x for x in range(10)]
print(num)

num = [x for x in range(100) if x%2 == 0]
print(num)