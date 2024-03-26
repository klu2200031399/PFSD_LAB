number_list = []
n = int(input("Enter the range: "))

for i in range(n):
    element = float(input("Enter element: "))
    number_list.append(element)


copied_list = number_list.copy() #copying the original list


if number_list:
    popped_element = number_list.pop()

result = sum(copied_list) / len(copied_list)
print("Original List:", number_list)
print("Popped Element:", popped_element if 'popped_element' in locals() else "List was empty")
print("Average of Copied List:", result)
