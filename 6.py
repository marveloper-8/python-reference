a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"a", "b", "c"}
d = {"c", "d", "e"}
e = {"f", "g", "c"}

# add
# a.add("orange")
# a.add("apple")
# print(a)

# clear
# a.clear()
# print(a)

# copy
# print(a.copy())

# difference
# print(a.difference(b))
# print(b.difference(a))

# difference update
# print(a.difference_update(b))

# discard
# a.discard("banana")
# print(a)

# intersection
print(a.intersection(b))
print(c.intersection(d, e))

# intersection update
print(a.intersection_update(b))
print(a)