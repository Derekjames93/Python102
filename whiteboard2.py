# Prompt user for input
print("Give me a number!")
# Create var for user input and store it as integer
user_input = int(input(' >'))
# Create a counter for loop
counter = 0




fib_list = [0,1]

# Create loop to take what the user input and have it check through the loop
while counter <= user_input :
    print(counter)
    new_eval = fib_list[-1] + fib_list [-2]
    fib_list.append(new_eval)
    counter += 1
    
print(fib_list)

     