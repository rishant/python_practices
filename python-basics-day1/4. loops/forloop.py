avangers = ["Ironman", "Captain America", "Thor", "Black Widow", "Hawk Eye", "Hulk"]

# Signle item read via INDEX
print(avangers[4], "\n")

# Read each item via loop
for name in avangers:
    print(name)

# list contains different datatypes elements
list = ["Ironman", 4, 35.8, ("Hawk", "Eye"), ["Hulk", "fulk", "sumk"], {"foo": "bar"}]
for item in list:
    print(item)
