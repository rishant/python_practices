empty_string = ''
empty_list = []
empty_dict = {}
bool_false = False
bool_true = True
full_string = 'test'
full_list = [1, 2, 3]
full_dict = {"key": "value"}
none = None
zero = 0
one = 1

def eval_as_true(iterable):
    """Exits on first False."""
    for element in iterable:
        if not element:
            return False
    return True

print('"Eval false items"')
things_that_are_false = [empty_string, empty_list, empty_dict, bool_false, none, zero]
print(eval_as_true(things_that_are_false) is False)
# True

print('\n"Eval true items"')
things_that_are_true = [full_dict, full_list, full_string, bool_true, one]
print(eval_as_true(things_that_are_true) is True)
# True

print('\n"Test if items equal True"')
for item in things_that_are_true:
    if item != True:
        print("%s does not equal 'True'!" % str(item))
    else:
        print("%s equals 'True'!" % str(item))
# {'key': 'value'} does not equal 'True'!
# [1, 2, 3] does not equal 'True'!
# test does not equal 'True'!
# True equals 'True'!
# 1 equals 'True'!

print('\n"Test if items ARE True"')
for item in things_that_are_true:
    if item is not True:
        print("%s is not 'True'!" % str(item))
    else:
        print("%s is 'True'!" % str(item))
# {'key': 'value'} is not 'True'!
# [1, 2, 3] is not 'True'!
# test is not 'True'!
# True is 'True'!
# 1 is not 'True'!

print('\n"Test item in itrable objects"')
print(2 in [1, 2, 3])
print('key2' in {'key1': 'value1', 'key2': 'value2'})
# True
# True

print('\n"Test ranges"')
print(1 < 5)
print(10 > 5)
print(1 < 5 < 10)
# True
# True
# True
