a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"a", "b", "c"}
d = {"c", "d", "e"}
e = {"f", "g", "c"}
f = {"google", "microsoft", "facebook"}
g = {"f", "e", "d", "c", "b", "a"}
h = {"f", "e", "d", "c", "b"}

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
# print(a.intersection_update(b))
# print(a)

# c.intersection_update(d, e)
# print(c)

# isdisjoint
print(a.isdisjoint(f))
print(a.isdisjoint(b))

# issubset
print(c.issubset(g))

# issuperset
print(g.issuperset(c))
print(h.issuperset(c))

# pop
# a.pop()
# print(a)
# print(a.pop())

# remove
# a.remove("banana")
# print(a)

# symmetric difference
print(a.symmetric_difference(b))