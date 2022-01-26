# absolute
print(abs(-7.25))
print(abs(3+5j))

# all
print(all([True, True, True]))
print(all([0, 1, 1]))
print(all((0, True, False)))
print(all({0, 1, 0}))
print(all({0: 'Apple', 1: 'Orange'}))

# any
print(any([False, True, False]))
print(any((0, 1, False)))
print(any({0, 1, 0}))
print(any({0: 'Apple', 1: 'Orange'}))

# ascii
print(ascii('My name is Ståle'))

# binary
print(bin(36))

# boolean
print(bool(1))

# bytearray
print(bytearray(4))

# bytes
print(bytes(4))

# callable
def a():
    b = 5
print(callable(a))

b = 5
print(callable(b))

# chr
print(chr(97))

# compile
c = compile('print(55)', 'test', 'eval')
exec(c)

d = compile('print(55)\nprint(88)', 'test', 'exec')
exec(d)

# complex
print(complex(3, 5))
print(complex('3+5j'))

# delattr
class A:
    name = 'John'
    age = 36
    country = 'Norway'

# delattr(A, 'age')

print(A.age)

# dict
print(dict(
    name="John",
    age=36,
    country="Norway"
))

# dir
print(dir(A))

# divmod
print(divmod(5, 2))

# zip
print(
    tuple(
        zip(
            ("John", "Charles", "Mike"),
            ("Jenny", "Christy", "Monica", "Vicky")
        )
    )
)

# vars
print(vars(A))

# type
print(type(('apple', 'banana', 'cherry')))
print(type("Hello World!"))
print(type(33))

# tuple
print(tuple(('apple', 'banana', 'cherry')))

# super
class B:
    def __init__(self, txt):
        self.message = txt

    def printmessage(self):
        print(self.message)

class C(B):
    def __init__(self, txt):
        super().__init__(txt)

e = C("Hello, and welcome!")
e.printmessage()

# sum
print(sum((1, 2, 3, 4, 5)))
print(sum((1, 2, 3, 4, 5), 7))

# str
print(str(3.5))
print(int("12"))

# sorted
print(sorted(("b", "g", "a", "d", "f", "c", "h", "e")))
print(sorted((1, 11, 2)))
print(sorted(("h", "b", "a", "c", "f", "d", "e", "g"), reverse=True))

# slice
f = ("a", "b", "c", "d", "e", "f", "g", "h")
# g = slice(2)
print(f[slice(2)])
print(f[slice(3, 5)])
print(f[slice(0, 8, 3)])

# set attr
setattr(A, 'age', 40)
print(getattr(A, 'age'))

# set
print(set(("apple", "banana", "cherry")))

# round
print(round(5.76543, 2))
print(round(5.76543))

# reversed
for a in reversed(["a", "b", "c", "d"]):
    print(a)

# range
for a in range(6):
    print(a)

for a in range(3, 6):
    print(a)

for a in range(3, 20, 2):
    print(a)

# print
print("Hello World")
print("Hello", "how are you?")
print(("apple", "banana", "cherry"))
print("Hello", "how are you?", sep="---")

# enumerate
# print(list(enumerate("apple", "banana", "cherry")))

# eval
eval('print(55)')

# exec
exec('name = "John"\nprint(name)')

# filter
g = [5, 12, 17, 18, 24, 32]
def h(a):
    if a < 18:
        return False
    else:
        return True

i = filter(h, g)
for a in i:
    print(a)

# float
print(float(3))
print(float("3.500"))

# format
print(format(0.5, "%"))
print(format(0.5, "<"))
print(format(0.5, ">"))
print(format(0.5, "^"))
print(format(0.5, "="))
print(format(0.5, "+"))
print(format(0.5, "-"))
print(format(0.5, " "))
print(format(34323, ","))
print(format(234234, "_"))
print(format(5, "b"))
print(format(32, "c"))
print(format(4, "d"))
print(format(5, "e"))
print(format(5, "E"))
print(format(25, "f"))
print(format(2.5, "F"))
print(format(2.5, "g"))
print(format(2.5, "G"))
print(format(2, "o"))
print(format(2, "x"))
print(format(3, "X"))
print(format(32, "n"))
print(format(53, "%"))

# frozenset
print(frozenset(["apple", "banana", "cherry"]))

# i = frozenset(["apple", "banana", "cherry"])
# i[1] = "strawberry"
# print(i)

# get attr
print(getattr(A, 'age'))
print(getattr(A, 'page', 'my message'))

# globals
print(globals())
print(globals()["__file__"])

# has attr
print(hasattr(A, 'age'))

# pow
print(pow(4, 3))
print(pow(4, 3, 5))

# ord
print(ord("h"))

# hex
print(hex(255))

# id
print(id(("apple", "banana", "cherry")))

# input
# print("Enter your name:")
# print("Hello, " + input())

# print("Hello, " + input('Enter your name'))

# int
print(int(3.5))
print(int("12"))

# is instance
print(isinstance(5, int))
print(isinstance("Hello", (float, int, str, list, dict, tuple)))
class D:
    name = "John"
j = D()
print(isinstance(j, D))

# is sub class
class E:
    age = 36

class F(E):
    name = "John"
    age = E

print(issubclass(F, E))

# iterator
k = iter(["apple", "banana", "cherry"])
print(next(k))
print(next(k))
print(next(k))

# len
print(len(["apple", "banana", "cherry"]))
print(len("Hello"))

# list
print(list(("apple", "banana", "cherry")))

# locals
print(locals())
print(locals()["__file__"])

# map
def l(a):
    return len(a)
print(map(l, ("apple", "banana", "cherry")))

def m(a, b):
    return a + b
print(map(m, ("apple", "banana", "cherry"), ("orange", "lemon", "pineapple")))

# max
print(max(5, 10))
print(max("Mike", "John", "Vicky"))
print(max((1, 5, 3, 9)))

# memory view
print(memoryview(b"Hello"))
print(memoryview(b"Hello")[0])
print(memoryview(b"Hello")[1])

# min
print(min(5, 10))
print(min("Mike", "John", "Vicky"))
print(min((1, 5, 3, 9)))

# next
m = iter(["apple", "banana", "cherry"])

# n = next(m)
# print(n)

# n = next(m)
# print(n)

# n = next(m)
# print(n)

o = next(m, "orange")
print(o)

o = next(m, "orange")
print(o)

o = next(m, "orange")
print(o)

o = next(m, "orange")
print(o)

# object
print(object())

# oct
print(oct(12))

# open
p = open("demofile.txt", "x")
print(f.create())