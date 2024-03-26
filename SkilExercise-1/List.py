number_list=[]
n=int(input("Enter the range"))
for i in range(n):
    number= float((input("Enter the list")))
    number_list.append(number)

result = sum(number_list)/len(number_list)
print(result)