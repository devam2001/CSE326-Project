print("Enter sides of a triangle: ")
x, y, z = int(input("Side 1: ")),int(input("Side 2: ")),int(input("Side 3: "))

if x == y and y == z and z == x:
    print("Equilateral Triangle.")
elif (x == y and z != x) or (y == z and y != x) or (z == x and z != y):
    print("Isosceles Triangle.")
else:
    print("Scalene Triangle.")

