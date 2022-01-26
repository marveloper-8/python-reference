# capitalize
print("hello, and welcome to my world.".capitalize())
print("python is FUN!".capitalize())
print("36 is my age.".capitalize())

# casefold
print("Hello, And Welcome To My World!".casefold())

# center
print("banana".center(20))
print("banana".center(20, "O"))

# count
print("I love apples, apple are my favourite fruit".count("apple"))
print("I love apples, apple are my favorite fruit".count("apple", 10, 24))

# encode
a = "My name is Ståle"
print(a.encode())
print(a.encode(encoding="ascii", errors="backslashreplace"))
print(a.encode(encoding="ascii", errors="ignore"))
print(a.encode(encoding="ascii", errors="namereplace"))
print(a.encode(encoding="ascii", errors="replace"))
print(a.encode(encoding="ascii", errors="xmlcharrefreplace"))

# ends with
b = "Hello, welcome to my world."
print(b.endswith("."))
print(b.endswith("my world."))
print(b.endswith("my world.", 5, 11))

# expand tabs
c = "H\te\tl\tl\to"
print(c.expandtabs(2))

print(c)
print(c.expandtabs())
print(c.expandtabs(2))
print(c.expandtabs(4))
print(c.expandtabs(10))

# find
print(b.find("welcome"))
print(b.find("e"))
print(b.find("e", 5, 10))
# print(b.find("q"))
# print(b.index("q"))

# format
print("For only {price:.2f} dollars!".format(price=49))
print("My name is {fname}, I'm {age}".format(fname="John", age=36))
print("My name is {0}, I'm {1}".format("John", 36))
print("My name is {}, I'm {}".format("John", 36))
print("We have {:<8} chickens.".format(49))
print("We have {:>8} chickens.".format(49))
print("We have {:^8} chickens.".format(49))
print("The temperature is {:=8} degrees celsius.".format(-5))
print("The temperature is between {:+} and {:+} degrees celsius.".format(-3, 7))
print("The temperature is between {:-} and {:-} degrees celsius.".format(-3, 7))