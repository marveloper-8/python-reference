# indentation
if 5 > 2:
    print("Five is greater than two!")

if 5 > 2:
 print("Five is greater than two!")

# comment
# This is a comment
print("Hello, World!") # This is another comment

# multiline comment

# This is a comment
# written in
# more than just one line

"""
This is a comment
written in
more than just one line
"""

# variables
a = 5
b = "John"
print(a)
print(b)

c = 4
c = "Sally"
print(c)

d = "John"
d = 'John'

# variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "john"
MYVAR = "John"
myvar2 = "John"

# 2myvar = "John"
# my-var = "John"
# my var = "John"

# assign values to multiple variables
e, f, g = "Orange", "Banana", "Cherry"
print(e)
print(f)
print(g)

h = i = j = "Orange"
print(h)
print(i)
print(j)

# output variables
print("Python is awesome")
print("My name is " + b)
print("My name is ", c)


# string concatenation
k = "Python is "
l = "awesome"
print(k + l)

m = "Hello"
n = "World"
print(m + " " + n)

o = 10
print(a + o)

# global variables
p = "awesome"
def q():
    global p
    p = "fantastic"
    # print("Python is " + p)

q()
print("Python is " + p)

# getting data types
print(type("Hello")) 
print(type(3))
print(type(3.14))
print(type(1j))
print(type(["apple", "banana", "cherry"]))
print(type(("apple", "banana", "cherry")))
print(type(range(6)))
print(type({"name": "John", "age": 36}))
print(type({"apple", "banana", "cherry"}))
print(type(True))
print(type(b"Hello"))
print(type(bytearray(5)))
print(type(memoryview(bytes(5))))

# setting data type
print(str("Hello World"))
print(type(str("Hello World")))

print(int(20))
print(type(int(20)))

print(int(20.5))
print(type(int(20.5)))

print(complex(1j))
print(type(complex(1j)))

print(list(("apple", "banana", "cherry")))
print(type(list(("apple", "banana", "cherry"))))

print(tuple(("apple", "banana", "cherry")))
print(type(tuple(("apple", "banana", "cherry"))))

print(range(6))
print(type(range(6)))

print(dict(name="John", age=36))
print(type(dict(name="John", age=36)))

print(set(("apple", "banana", "cherry")))
print(type(set(("apple", "banana", "cherry"))))

print(frozenset(("apple", "banana", "cherry")))
print(type(frozenset(("apple", "banana", "cherry"))))

print(bool(5))
print(type(bool(5)))

print(bytes(5))
print(type(bytes(5)))

print(bytearray(5))
print(type(bytearray(5)))

print(memoryview(bytes(5)))
print(type(memoryview(bytes(5))))

# Numbers
print(type(1))
print(type(2.8))
print(type(1j))

# int
print(type(1))
print(type(35656222554887711))
print(type(-3255522))

# floats
print(type(1.10))
print(type(1.0))
print(type(-35.59))

print(35e3)
print(type(35e3))

print(12E4)
print(type(12E4))

print(-87.7e100)
print(type(-87.7e100))

# complex
print(3+5j)
print(type(3+5j))

print(5j)
print(type(5j))

print(-5j)
print(type(-5j))

# type conversion
r = 1
s = 2.8
t = 1j

u = float(r)
v = int(s)
w = complex(t)

print(u)
print(v)
print(w)

print(type(u))
print(type(v))
print(type(w))

# random number
import random
print(random.randrange(1, 10))

# specifiy variable type
print(int(1))
print(int(2.8))
print(int("3"))

print(float(1))
print(float(2.8))
print(float("3"))
print(float("4.2"))

print(str("s1"))
print(str(2))
print(str(3.0))

# string literals
print("Hello")
print('Hello')

# string variables
x = "Hello"
print(x)

# multi line strings
print("""
Hello
How
are
you
""")

print('''
I
am
fine
thank
you
''')

# strings as arrays
print("Hello, World!"[1])

# string slices
print("Hello, World!"[2:5])

# string negative indexing
print("Hello, World!"[-5:-2])

# string length
print(len("Hello, World!"))

# check string
print("ain" in "The rain in Spain stays mainly in the plain")
print("ain" not in "The rain in Spain stays mainly in the plain")

# format a string
print("My name is John, and I am {}".format(36))
print("I want {} pieces of item {} for {} dollars.".format(3, 567, 49.95))
print("I want to pay {2} dollars for {0} pieces of item {1}.".format(3, 567, 49.95))

# escape character
print("We are the so-called \"Vikings\" from the north.")
print('It\'s alright.')
print("This will insert one \\ (backlash).")
print("Hello\nWorld!")
print("Hello\rWorld!")
print("Hello\tWorld!")
print("Hello \bWorld!")
print("\110\145\154\154\157")
print("\x48\x65\x6c\x6c\x6f")

# boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

if 33 > 200:
    print("33 is greater than 200")
else:
    print("33 is not greater than 200")

# evaluate boolean values
print(bool("Hello"))
print(bool(15))

y = "Hello"
z = 15

print(bool(y))
print(bool(z))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class aa():
    def __len__(self):
        return 0

print(bool(aa()))

# return boolean
def ab():
    return True

print(ab())

if ab():
    print("YES!")
else:
    print("NO!")

print(isinstance(200, int))

# operators
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(12 / 3)
print(5 % 2)
print(5 ** 2)
print(15 // 2)

# assignment operators
ac = 5
# ac += 3
# ac -= 3
# ac *= 3
# ac /= 3
# ac %= 3
# ac //= 3
# ac **= 3
# ac &= 3
# ac |= 3
# ac ^= 3
# ac >>= 3
# ac <<= 3

print(ac)

# comparison operators
print(5 == 3)
print(5 != 3)
print(5 > 3)
print(5 < 3)
print(5 >= 3)
print(5 <= 3)

# logical operators
print(ac > 3 and ac < 10)
print(ac > 3 or ac < 4)
print(not(ac > 3 and ac < 10))

# identity operators
ad = ["apple", "banana"]
ae = ["apple", "banana"]
af = ad
print(ad is ae)
print(ad is af)

print(ad is not ae)
print(ad is not af)

# membership operators
print("banana" in ad)
print("orange" not in ad)

# lists
print(["apple", "banana", "cherry"])

# access list items
print(["apple", "banana", "cherry"][1])
print(["apple", "banana", "cherry"][-1])
print(["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"][2:5])
print(["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"][:4])
print(["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"][2:])
print(["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"][-4:-1])

# change list items
ag = ["apple", "banana", "cherry"]
# ag[1] = "blackcurrant"
print(ag)

# loop list items
for a in ag:
    print(a)

# list comprehension
ah = ["apple", "banana", "cherry", "kiwi", "mango"]
ai = [a for a in ah if "a" in a]
print(ai)

# for a in ah:
#     if "a" in a:
#         ai.append(a)
# print(ai)

# check if list item exists
if "apple" in ag:
    print("Yes, 'apple' is in the fruits list")

# list length
print(len(ag))

# add list items
# ag.append("orange")
ag.insert(1, "orange")
print(ag)

# remove items from list
ag.remove("banana")
print(ag)

ag.pop()
print(ag)

del ag[0]
print(ag)

# del ag
ag.clear()
print(ag)

# copy list
aj = ["apple", "banana", "cherry"]
print(aj.copy())
print(list(aj))

# join list
ak = ["a", "b", "c"]
al = [1, 2, 3]
print(ak + al)

# for a in al:
#     ak.append(a)

ak.extend(al)
print(ak)

# tuple
print(("apple", "banana", "cherry"))

# access tuple items
print(("apple", "banana", "cherry")[1])
print(("apple", "banana", "cherry")[-1])
print(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")[2:5])
print(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")[-4:-1])

# change tuple items
al = ("apple", "banana", "cherry")
am = list(al)
am[1] = "kiwi"
print(tuple(am))

# loop tuple items
for a in al:
    print(a)

# check if tuple item exists
if "apple" in al:
    print("Yes, 'apple' is in the fruits tuple")

# tuple length
print(len(("apple", "banana", "cherry")))

# tuple with one item
print(type(("apple",)))
print(type(("apple")))

# remove tuple item
# an = ("apple", "banana", "cherry")
# del an
# print(an)

# join tuples
print(("a", "b", "c") + (1, 2, 3))

# set
print({"apple", "banana", "cherry"})

# access set items
for a in {"apple", "banana", "cherry"}:
    print(a)

print("banana" in {"apple", "banana", "cherry"})

# add set items
an = {"apple", "banana", "cherry"}
an.add("orange")
print(an)

an.update(["mango", "grapes"])
print(an)

# loop set items
for a in an:
    print(a)

print("banana" in an)

# check if an item exists in a set
if "apple" in an:
    print("Yes, 'apple' is in this set")

# set length
print(len(an))

# remove set item
an.remove("banana")
print(an)

# join sets
print({"a", "b", "c"}.union({1, 2, 3}))

ao = {"a", "b", "c"}
ap = {1, 2, 3}

ao.update(ap)
print(ao)

# dictionaries
aq = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(aq)
print(aq["model"])
print(aq.get("model"))

# access dictionary items
print(aq["model"])
print(aq.get("model"))

# change dictionary item
aq["year"] = 2018
print(aq)

# loop dictionary items
for a in aq:
    print(a)

for a in aq:
    print(aq[a])

for a in aq.values():
    print(a)

for a, b in aq.items():
    print(a, b)

# check if dictionary item exist
if "model" in aq:
    print("Yes 'model' is one of the keys in the dictionary")

# dictionary length
print(len(aq))

# add item to dictionary
aq["color"] = "red"
print(aq)

# remove an item from a dictionary
aq.pop("model")
print(aq)

aq.popitem()
print(aq)

del aq["brand"]
print(aq)

aq.clear()
print(aq)

# copy dictionaries
ar = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(ar.copy())
print(dict(ar))

# nested dictionaries
at = {
    "au": {
        "name": "Emil",
        "year": 2004
    },
    "av": {
        "name": "Tobias",
        "year": 2007
    },
    "aw": {
        "name": "Linus",
        "year": 2011
    }
}

print(at)

ax = {
    "name": "Emil",
    "year": 2004
}

ay = {
    "name": "Tobias",
    "year": 2007
}

az = {
    "name": "Linus",
    "year": 2011
}

ba = {
    "bb": ax,
    "bc": ay,
    "bd": az
}
print(ba)

# if statement
if 200 > 33:
    print("200 is greater than 33")

# elif
if 33 > 33:
    print("33 is greater than 33")
elif 33 == 33:
    print("33 and 33 are equal")

# else
bb = 200
bc = 33
bd = 300

if bc > bb:
    print("bc is greater than bb")
elif bb == bc:
    print("bb and bc are equal")
else:
    print("bb is greater than bc")

if bc > bb:
    print("bc is greater than bb")
else:
    print("bc is not greater than bb")

# shorthand if
if bb > bc: print("bb is greater than bc")

# shorthand if else
print("A") if bb > bc else print("B")
print("A") if bb > bc else print("=") if bb == bc else print("B")

# if and
if bb > bc and bd > bb:
    print("Both conditions are True")

# if or
if bb > bc or bb > bd:
    print("At least one of the conditions is True")

# if nested
if 41 > 10:
    print("Above ten,")
    if 41 > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# if pass
if bb > bc:
    pass

# while
be = 1
# while be < 6:
#     print(be)
#     be += 1

# while break
# while be < 6:
#     print(be)
#     if be == 3:
#         break
#     be += 1

# while continue
# while be < 6:
#     be += 1
#     if be == 3:
#         continue
#     print(be)

# while else
while be < 6:
    print(be)
    be += 1
else:
    print("be is no longer less than 6")

# for
bd = ["apple", "banana", "cherry"]
for a in bd:
    print(a)

# for string
for a in "banana":
    print(a)

# for break
# for a in bd:
#     if a == "banana":
#         break
#     print(a)

# for continue
for a in bd:
    if a == "banana":
        continue
    print(a)