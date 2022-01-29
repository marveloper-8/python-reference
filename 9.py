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
print("Hello World")
print(type("Hello World"))

print(20)
print(type(20))

print(20.5)
print(type(20.5))

print(1j)
print(type(1j))

print(["apple", "banana", "cherry"])
print(type(["apple", "banana", "cherry"]))

print(("apple", "banana", "cherry"))
print(type(("apple", "banana", "cherry")))

print(range(6))
print(type(range(6)))