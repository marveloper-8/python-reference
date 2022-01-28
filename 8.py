import calendar as c

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