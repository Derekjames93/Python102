list_one = [1,4,7]
list_two = [5,8,3]


new_list = []

for num1, num2 in zip(list_one,list_two):
    new_list.append(num1 * num2)
print(new_list)
