a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
c = [1, 4, 2, 9, 7, 8, 9, 3, 1]
e = (1, 4, 5, 9)
f = [4, 55, 64, 32, 16, 32]

def d(a):
    return len(a)
g = ["Ford", "Mitsubishi", "BMW", "VW"]
g.sort(key=d)
print(g)

def h(a):
    return a['year']
i = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]
i.sort(key=h)
print(i)

# b.sort(reverse=True)
# print(b)

# a.reverse()
# print(a)

# a.remove("banana")
# print(a)

# print(a.pop(1))

# a.pop(1)
# print(a)

# a.insert(1, "orange")
# print(a)

# d = a.copy()
# print(d)

# print(a.count("cherry"))

# print(c.count(9))

# a.extend(e)
# print(a)

# print(a.index("cherry"))
# print(f.index(32))

# a.extend(b)
# print(a)

# a.append("orange")
# print(a)

# a.append(b)
# print(a)

# a.clear()
# print(a)