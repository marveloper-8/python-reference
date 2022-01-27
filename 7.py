a = open("demofile.txt", "r")

# print(a.read())
# a.close()

# print(a.fileno())

# b = open("myfile.txt", "a")
# b.write("Now the file has one more line!")
# b.flush()
# b.write("...add another one!")

# print(a.isatty())
# print(a.read())
# print(a.read(33))
# print(a.readable())

print(a.readline(5))
# print(a.readline())