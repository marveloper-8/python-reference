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