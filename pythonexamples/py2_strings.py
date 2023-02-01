print('"Single line strings"')
var1 = "Strings can use double quotes."
var2 = 'Strings can use single quotes.'
print(var1)
print(var2)
# Strings can use double quotes.
# Strings can use single quotes.

print('\n"Slice strings"')
var1 = "Slice this string."
print(var1[6:10])
# this

print('\n"Slice strings with steps"')
var1 = "Slice this string with steps."
print(var1[6:10:2])
# ti

print('\n"Tripple quoted strings."')
var1 = '''We don't have to escape 'single quotes' in a tripple quoted string'''
var2 = '''We can do multiline
strings as well.
'''
print(var1)
print(var2)
# We don't have to escape 'single' quotes in a tripple quoted string
# We can do multiline
# strings as well.

print('\n"Raw strings."')
import re
var1 = re.sub('(\\w)', '[\\1]', 'Words and numbers: 12345!')
var2 = re.sub(r'(\w)', r'[\1]', 'Words and numbers: 12345!')
print(var1)
print(var2)

# [W][o][r][d][s] [a][n][d] [n][u][m][b][e][r][s]: [1][2][3][4][5]!
# [W][o][r][d][s] [a][n][d] [n][u][m][b][e][r][s]: [1][2][3][4][5]!

print('\n"Byte strings."')
var1 = "Python3 strings are Unicode by default: \u260E."
var2 = b"Python3 strings are Unicode by default: \xe2\x98\x8e."
print(var1 == var2.decode('utf-8'))
print(var1.encode('utf-8') == var2)
# True
# True

print('\n"String formatting"')
print('0x%04x %s' % (37, "some string"))
# 37 some string
print('0x{:04x}, {}'.format(37, 'some string'))

print('\n"Python 3.6 f-strings"')
value = 3.6
string = "Python"
print(f'f-strings in {string} {value:g}')
# f-strings in Python 3.6
