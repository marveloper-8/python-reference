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
print("The temperature is between {: } and {: } degrees celsius.".format(-3, 7))
print("The universe is {:,} years old.".format(13800000000))
print("The universe is {:_} years old.".format(13800000000))
print("The binary version of {0} is {0:b}".format(5))
print("We have {:d} chickens.".format(0b101))
print("We have {:e} chickens.".format(5))
print("We have {:E} chickens.".format(5))
print("The price is {:.2f} dollars.".format(45))
print("The price is {:f} dollars.".format(45))
print("The octal version of {0} is {0:o}".format(10))
print("The Hexadecimal version of {0} is {0:x}".format(255))
print("The Hexadecimal version of {0} is {0:X}".format(255))
print("You scored {:%}".format(0.25))
print("You scored {:.0%}".format(0.25))

# index
print(b.index("welcome"))
print(b.index("e", 5, 10))
# print(b.find("q"))
# print(b.index("q"))

# isalnum
print("Company12".isalnum())
print("Company 12".isalnum())

# isalpha
print("CompanyX".isalpha())
print("Company10".isalpha())

# zfill
print("50".zfill(10))
print("hello".zfill(10))
print("welcome to the jungle".zfill(10))
print("10.000".zfill(10))

# upper
print("Hello my friends".upper())

# translate
print("Hello Sam!".translate({83: 80}))
print("Hello Sam!".translate("Hello Sam!".maketrans("S", "P")))
print("Good night Sam!".translate("Good night Sam!".maketrans("mSa", "eJo", "odnght")))
print("Good night Sam!".translate({
    109: 101,
    83: 74,
    97: 11,
    111: None,
    100: None,
    110: None,
    103: None,
    104: None,
    116: None
}))

# title
print("Welcome to my world".title())
print("Welcome to my 2nd world".title())
print("hello b2b2b2 and 3g3g3g".title())

# swapcase
print("Hello My Name is PETER".swapcase())

# strip
print("of all fruits", "     banana     ".strip(), "is my favorite")
print(",,,,,rrttgg.....banana.....rrr".strip(",.grt"))

# startswith
print("Hello, welcome to my world.".startswith("Hello"))
print("hello, welcome to my world.".startswith("wel", 7, 20))

# splitlines
print("Thank you for the music\nWelcome to the jungle".splitlines())
print("Thank you for the music\nWelcome to the jungle".splitlines(True))

# split
print("welcome to the jungle".split())
print("hello, my name is Peter, I am 26 years old".split(", "))
print("apple#banana#cherry#orange".split("#"))
print("apple#banana#cherry#orange".split("#", 1))

# rstrip
print("of all fruits", "     banana     ".rstrip(), "is my favourite")