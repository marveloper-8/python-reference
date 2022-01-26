a = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
b = ('key1', 'key2', 'key3')

# fromkeys
print(dict.fromkeys(b, 0))
print(dict.fromkeys(b))

# copy
print(a.copy())

# clear
# a.clear()
# print(a)