f = open("file.txt", "r")  # opening the file
print(f.read())  # reading all the contents of the file
print(f.read())  # reading the contents of the file
print(f.read(5))  # reading the first 5 chars in the file
print(f.readline())  # read the first of the file


# Writing in an existing file
f = open("file.txt", "w")
f.write("File is updated")
f = open("file.txt", "r")
print(f.read())


# Writing the New File
f = open("sample.txt", "w")
f.write("New file is created successfully")
f = open("sample.txt", "r")
print(f.read())
f.close()

# Append for the existing file
f1 = open("sample.txt", "a")
f1.write("More data is added now")
f1= open("sample.txt", "r")
print(f1.read())
