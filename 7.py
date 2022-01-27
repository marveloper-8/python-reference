a = open("demofile.txt", "r")
b = open("demofile2.txt", "a")

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

# print(a.readline(5))
# print(a.readline())

# print(a.readlines(33))
# a.seek(4)
# print(a.readline())
# print(a.seek(4))
# print(a.seekable())
# print(a.readline())
# print(a.tell())
# print()

# b.truncate(20)
# b.close()

# b = open("demofile2.txt", "r")
# print(b.read())

print(b.writable())