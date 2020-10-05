print("Set the password:")
password = input()
count = 0
while True:
    t = input("Enter password: ")
    if password != t:
        count += 1
    else:
        print("You have successfully logged In")
        exit(0)
    if count > 3:
        print("You have been denied access")
        exit(0)

