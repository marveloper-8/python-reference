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
assert a == "goodbye", "a should be 'hello'"