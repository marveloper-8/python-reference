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
ac -= 3

print(ac)