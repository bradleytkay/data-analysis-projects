# Exercise #1: Construct for loops that accomplish the following tasks:
    # a. Print the numbers 0 - 20, one number per line.
    # b. Print only the ODD values from 3 - 29, one number per line.
    # c. Print the EVEN numbers 12 to -14 in descending order, one number per line.
    # d. Challenge - Print the numbers 50 - 20 in descending order, but only if the numbers are multiples of 3. (Your code should work even if you replace 50 or 20 with other numbers).


#a
for num in range(0, 21, 1):
    print(num); 

#b
for num in range(3, 29, 3):
    if num % 2 == 1:
        print(num); 

#c
num = 12
decrease_by = 2

while num <= 12:
    num -= decrease_by
    print(num)

    if num <= -14:
        break; 

#d
num = 50
decrease_by = 1

while num <= 50:
    num -= decrease_by
    if num % 3 == 0:
        print(num)

    if num <= 20:
        break;

