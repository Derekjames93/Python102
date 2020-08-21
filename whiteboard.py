# Prompt user for input
print("Give me a number!")

# Create var for user input and store it as integer
user_input = int(input(' >'))
# Create a counter for loop
counter = 0
# Create loop to take what the user input and have it check through the loop
while counter <= user_input :
    if counter % 3 == 0 and counter % 5 == 0:
            print("fizzbuzz")
    elif counter % 3 == 0:
            print("fizz") 
    elif counter % 5 == 0:
            print("buzz")
    print(counter)
    counter += 1
