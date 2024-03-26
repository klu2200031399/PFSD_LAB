print("-->Finding the average")
x=(10,20,30,40,50)
z=sum(x)/len(x)
print(z)
print(type(x))

print("-->Input given through compiler")
a=int(input("Enter the First number"))
b=int(input("Enter the Secound number"))

print(a,b)

print("-->Adding two integers")
a1=20
a2=30
print(a1+a2)

print("-->Adding two flaot numbers")
a3=10.8
a4=3.9
print(a3+a4)

print("-->Adding two complex numbers")
a5=12+8j
a6=13+9j
print(a5+a6)

print("--->converting integer to float")
a7=10
print(float(a7))


print("-->Program to perform addition of string and integer using explict conversion")
p=input("Enter the number")
print(type(p))
q=int(input("Enter the number"))
print(type(q))
result=int(p)+q
print(result)
print(type(result))
