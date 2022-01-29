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