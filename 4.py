a = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
b = ('key1', 'key2', 'key3')

# setdefault
print(a.setdefault("model", "Bronco"))
print(a.setdefault("color", "white"))

# popitem
# a.popitem()
# print(a.popitem())

# pop
# a.pop("model")
# print(a.pop("model"))

# fromkeys
# print(dict.fromkeys(b, 0))
# print(dict.fromkeys(b))

# copy
# print(a.copy())

# clear
# a.clear()
# print(a)