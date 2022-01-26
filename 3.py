a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
c = [1, 4, 2, 9, 7, 8, 9, 3, 1]
e = (1, 4, 5, 9)

d = a.copy()
print(d)

print(a.count("cherry"))

print(c.count(9))

a.extend(e)
print(a)

# a.extend(b)
# print(a)

# a.append("orange")
# print(a)

# a.append(b)
# print(a)

# a.clear()
# print(a)