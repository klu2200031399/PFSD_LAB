

#pattren
print("--->4. Write a Python program to construct the following pattern, using a nested for loop.")
n=int(input("Enter the number :"))
for i in range(0,n):
    for j in range (0,i+1):
        print("*" ,end="")
    print('\r')

for i in range(0,n):
    for j in range (i-n-1,0-2):
        print("*" ,end="")
    print('\r')

print("--->3.Given triangle is a Right-triangle or not")
def triangle(side1, side2, side3):

    sides = sorted([side1, side2, side3])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False


side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))


if triangle(side1, side2, side3):
    print("It is a right triangle.")
else:
    print("It is not a right triangle.")

print("--->2. Program to display the first 7 multiples of 7.")
for i in range(1, 8):
    multiple = 7 * i
    print(f"Multiple {i}: {multiple}")

print("--->1. Program in Python to display the Factorial of a number.")


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:

    for i in range(n):
        result = n * n - 1


print(result)






