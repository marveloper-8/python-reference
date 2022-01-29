import calendar as c
from typing import Type

# and
print((5 > 3 and 5 < 10))
if 5 > 3 and 5 < 10:
    print("Both statements are True")
else:
    print("At least one of the statements are False")

# as
print(c.month_name[1])

# assert
a = "hello"

assert a == "hello"
# assert a == "goodbye", "a should be 'hello'"

# break
for a in range(9):
    if a > 3:
        break
    print(a)

b = 1
while b < 9:
    print(b)
    if b == 3:
        break
    b += 1

# class
class A:
    name = "John"
    age = 36

print(A.name)
print(A().name)

# continue
for a in range(9):
    if a == 3:
        continue
    print(a)

c = 0
while c < 9:
    c += 1
    if c == 3:
        continue
    print(c)

# def
def d():
    print("Hello from a function")
d()

# del
class B:
    name = "John"
# del B
print(B)

e = "hello"
# del e
print(e)

f = ["apple", "banana", "cherry"]
# del f[0]
print(f)

# elif
for a in range(-5, 5):
    if a > 0:
        print("YES")
    elif a == 0:
        print("WHATEVER")
    else:
        print("NO")

# else
g = 2
if g > 3:
    print("YES")
else:
    print("NO")

h = 5
try:
    h > 10
except:
    print("Something went wrong")
else:
    print("The 'Try' code was executed without raising any errors!")

# except
try:
    i > 3
except:
    print("Something went wrong")

j = "hello"
try:
    j > 3
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You are comparing values of different type")

try:
    k = 1/0
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You are comparing values of different type")
except:
    print("Something else went wrong")

l = 1
try:
    l > 10
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You are comparing values of different type")
else:
    print("The 'Try' code was executed without raising any errors!")

# false
print(5 > 6)
print(4 in [1, 2, 3])
print("hello" is "goodbye")
print(5 == 6)
print(5 == 6 or 6 == 7)
print(5 == 6 and 6 == 7)
print("hello" is not "hello")
print(not(5 == 5))
print(3 not in [1, 2, 3])

# finally
try:
    m > 3
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The try...except block is finished")

# for
for a in range(1, 9):
    print(a)

for a in f:
    print(a)

# from
from datetime import time
print(time(hour=15))

# global
def n():
    global o 
    o = "hello"

n()
print(o)

# if
p = 5
if p > 3:
    print("YES")

if p > 6:
    print("YES")
else:
    print("NO")

# import
import datetime
print(datetime.datetime.now())

# in
if "banana" in f:
    print("yes")

for a in f:
    print(a)

# is
m = f
print(m is f)

q = ["apple", "banana", "cherry"]
print(f is q)

# lambda
r = lambda a : a + 10
print(r(5))

s = lambda a, b, c: a + b + c
print(s(5, 6, 2))

# none
print(None)

t = None

if t:
    print("Do you think None is True?")
elif t is False:
    print("Do you think None is False?")
else:
    print("Non is not True, or False, None is just None...")

# nonlocal
def u():
    v = "John"
    def w():
        # nonlocal v
        v = "hello"
    w()
    return v

print(u())

# not
print(not False)

# or
print((5 > 3 or 5 > 10))

if 5 > 3 or 5 > 10:
    print("At least one of the statements are True")
else:
    print("None of the statements are True")

# pass
for a in [0, 1, 2]:
    pass

def x():
    pass

class y():
    pass

if 33 > 200:
    pass

# raise
# if -1 < 0:
#     raise Exception("Sorry, no numbers below zero")

# if not type("hello") is int:
#     raise TypeError("Only integers are allowed")

# return
def z():
    return 3 + 3

print(z())