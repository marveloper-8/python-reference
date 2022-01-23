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
class Person:
    name = 'John'
    age = 36
    country = 'Norway'

# delattr(Person, 'age')

print(Person.age)

print(dict(
    name="John",
    age=36,
    country="Norway"
))

print(dir(Person))