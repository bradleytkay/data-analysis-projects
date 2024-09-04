# 1) We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.

def reverse_characters(string):  

# b) Within the function, use the 'list' function to split a string into a list of individual characters

    list_characters = list(string)
    print(list_characters)

# c) 'reverse' your new list.

    list_characters.reverse()
    print(list_characters)

# d) Use 'join' to create the reversed string and return that string from the function.

    reversed_string = ''.join(list_characters)
    print(reversed_string)

    return reversed_string

# e) Create a variable of type string to test your new function. # f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.

string = 'ABCDEFG'
print(reverse_characters(string)); 
# Q: why is this returning None when the function itself is working, as evidenced by the print() statements
# I put throughout to check each element? 
# A: because I didn't have a return statement at the end of the function

# g) Use method chaining to reduce the lines of code within the function.

def rev_char(string):
    list_char = list(string)
    rev_list = ''.join(reversed(list_char))
    return rev_list

string = 'HIJKLMNOP'
print(rev_char(string))

# -OR- 

def rev_char_2(string):
    rev_list_char = ''.join(list(string)[::-1])
    return rev_list_char

string = 'HIJKLMNOP'
print(rev_char_2(string)) 

# Q: Why is this function only 'doing anything' when the print(rev_char(string)) function is called?
# Shouldn't print(rev_list) on line 34 do something on its own? 
# A: Again, I didn't have return statements


# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")

# a) Add an if statement to your reverse_characters function to check the typeof the parameter.

# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.

def rev_char_type(string):
    if type(string) == str:
        list_characters = list(string)
        list_characters.reverse()
        reversed_string = ''.join(list_characters)
    elif type(string) == int:
        int_str = str(string)
        list_characters = list(int_str)
        list_characters.reverse()
        reversed_string = ''.join(list_characters)
        int(reversed_string)
    return reversed_string

string = 12345567
print(rev_char_type(string))

# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.

# 3) Create a new function with one parameter, which is the list we want to change. The function should:

# a) Define and initialize an empty list.

def list_func(list):
    new_list = []
#     return new_list

# print(list_func(list))

# b) Loop through the old list.

    for i in list:

# c) For each element in the old list, call reverse_characters to flip the characters or digits.

        rev_i = rev_char_type(i)

# d) Add the reversed string (or number) to the list defined in part ‘a’.

        new_list.insert(0, rev_i)

# e) Return the final, reversed list.

    return new_list

# f) Be sure to print the results from each test case in order to verify your code.

list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']

print(list_func(list_test1))
print(list_func(list_test2))
print(list_func(list_test3))