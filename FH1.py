# Write a program for file handling using read, write and append

f = open("file.txt", "r")
print(f.read())
print(f.read())
print(f.readline())

f = open("file.txt", "w")
f.write(" File is updated")

f = open("file.txt", "a")
f.write("Append line")
f.close()


