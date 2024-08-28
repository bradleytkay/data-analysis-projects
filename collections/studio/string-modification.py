my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

new_string = my_string[3:] + my_string[0:3]
print(new_string)

# Use a template literal to print the original and modified string in a descriptive phrase.

print(f'{my_string} is correct.  {new_string} is not.')

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

user_input = int(input('How many letters would you like to replace:  '))

new_string = my_string[user_input:] + my_string[0:user_input]
print(new_string)

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

while True:
    if user_input <= 12:
        break
    else:
        user_input == 3
        print('Try again with a number between 0 and 12.')
    

