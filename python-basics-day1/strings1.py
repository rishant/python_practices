# String is immutable

# st = "rishant"
st = "rishant gupta"

# Show all method using built-in methods dir()
print(dir(st))

print(st.isalnum()) #Output: False
print(st.isalpha()) #Output: False
print(st.isdigit()) #Output: False
print(st.islower()) #Output: True
print(st.isupper()) #Output: False

# search string in other string
print('z' in st)
print('z' not in st)

print(st.lower()) #Output: rishant gupta
print(st.upper()) #Output: RISHANT GUPTA
print(st.capitalize()) #Output: Rishant gupta

print(st.join("0123456789")) #Output: 0rishant gupta1rishant gupta2rishant gupta3rishant gupta4rishant gupta5rishant gupta6rishant gupta7rishant gupta8rishant gupta9

print(st.split(' ')) #Output: ['rishant', 'gupta']
print(st.count('r')) #Output: 1

# String iterations
# for i in st:
#     print(i)
print(st[0]) #start index char -> #Output: r
print(st[-1]) #last index char -> #Output: a
print(st[5:len(st)]) #start index to end index char's -> #Output: nt gupta
print(st[:len(st)-4]) #start index 0 to end index -4 char's -> #Output: rishant g
print(st[3:]) #start index 3 to end index char's -> #Output: hant gupta
print(st[3:len(st):3]) #start index 5 to end index char's using skipping 2 char's include 3 one index's -> #Output: htua

# Space triming
st = "  ABCDE$#@%   "
print(st.lstrip())
print(st.rstrip())
print(st.strip())