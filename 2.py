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