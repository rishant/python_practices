fruit = ('apple', 'banana', 'watermellon', 'pear', 'orange')

print('"Find fruit with for loop"')
def find_fruit(fruit, fruits_we_want):
    is_fruit = (
        'apple', 'banana', 'watermellon', 
        'pear', 'orange', 'kiwi', 'cherry', 'mango'
    )
    for target_fruit in fruits_we_want:
        if target_fruit not in is_fruit:
            print('%s is not a fruit!' % target_fruit)
        elif target_fruit in fruit:
            print('found %s' % target_fruit)
        else:
            print('couldn\'t find %s.' % target_fruit)

find_fruit(fruit, ('banana', 'pear', 'cherry'))
find_fruit(fruit, ('apple', 'carrot'))
# found banana
# found pear
# couldn't find cherry.
# found apple
# carrot is not a fruit!

print('\n"Find a banana with while loop"')
index = len(fruit) - 1
while index > 0:
    if fruit[index] != 'banana':
        index -= 1
        continue
    print('We found a banana!')
    break
# We found a banana!

print('\n"Single line statements"')
var1 = 'True' if 3 < 5 else 'False'
var2 = [x for x in range(10) if not x % 2]
print(var1)
print(var2)
# True
# [0, 2, 4, 6, 8]
