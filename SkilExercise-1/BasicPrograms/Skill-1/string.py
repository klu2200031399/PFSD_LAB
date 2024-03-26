# example2

"""x = 0
str1 = "thisismycountryindia"
for i in str1:
    x = x +1
    print(str1[0:x])
for i in str1:
    x = x -1
    print(str1[0:x])"""

#pattren
n=int(input("Enter the number :"))
for i in range(0,n):
    for j in range (0,i+1):
        print("*" ,end="")
    print('\r')

for i in range(0,n):
    for j in range (i-n,0):
        print("*" ,end="")
    print('\r')

#example to convert binary
a=1045
a2=format(a,'b')
print(a2)
a3=format(a,'d')
print(a3)
x=hex(123456)
print(x)

a1=1045
a3="10110"
a2=int(format(int(a3,2),'d'))
print(a2)