proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.

comma = ','
semicolon = ';'
space = ' '

for string in strings: 
    if comma in string:
        print('comma')
    elif semicolon in string:
        print('semicolon')
    elif space in string:
        print('space')

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.

for string in strings:
    if comma in string:
        array = string.split(',')
        array.reverse()
        comma_reversed_string = ','.join(array)
        print(comma_reversed_string)

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.

for string in strings:
    if semicolon in string:
        array = string.split(';')
        array.sort()
        comma_sorted_string = ','.join(array)
        print(comma_sorted_string)

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

for string in strings:
    if space in string:
        array = string.split(' ')
        array.sort()
        array.reverse()
        comma_sorted_reversed_string = ' '.join(array)
        print(comma_sorted_reversed_string)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.

comma_space = 'Comma-spaces'

for string in strings:
    if comma_space in string:
        array = string.split(',')
        array.reverse()
        comma_reversed_string = ','.join(array)
        print(comma_reversed_string)