# Created a list of numbers
list_numbers = [20,50,62,64,30,67,23]

#Create a For loop using var = num
 # This takes all values inside list_numbers and applies it to var num
 # This is stating that if the remainder of num divided by 2 does not equal 0 then print num
for num in list_numbers :  
    if num % 2== 0 :   
        print(num)


for num in list_numbers :  
    is_even = num % 2==0
    if is_even : 
        print(num)