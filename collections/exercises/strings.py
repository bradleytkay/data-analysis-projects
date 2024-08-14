# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.

new_text = text[0:12]
print(new_text)

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!

newer_text = text[-12:]
print(newer_text)

# 3. Print a slice of the middle 12 characters from 'text'.

newest_text = text[12:24]
print(newest_text)

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.

my_string = 'word'
for char in my_string:
    print('\t' + char)

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.

text = 'word'
reversed_text = text[::-1]
print(reversed_text)

text = 'word'
reversed_text = ''
for char in text: 
    reversed_text = char + reversed_text
print(reversed_text)

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').

text = 'tomato'
reversed_text = text[::-1]
print(text + reversed_text)
print(text + ' | ' + reversed_text)