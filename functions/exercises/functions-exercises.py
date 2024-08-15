# Part 1 A -- Make a Line

def make_line(size):
    line = ''
    for i in range(size):
        line += "#" 
    return line

print(make_line(5))

#I didn't get and don't think I would've ever been able to get this solution
#without checking the provided solution in Canvas, which is discouraging. 

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square

def make_square(size):
    square = ''
    for i in range(size):
        square += make_line(size) + '\n'
    return square

print(make_square(5))

#It took me a hot minute to figure out how to incorporate the newline character (\n)
#I didn't realize it had to be concatenated as a string of its own... 

# Part 1 C -- Make a Rectangle

def make_rectangle(height, width):
    rectangle = ''
    for i in range(height):
        rectangle += (make_line(width) * 3) + '\n'
    return rectangle

print(make_rectangle(3, 5))


# def make_rectangle(size):
#     rectangle = ''
#     for i in range(size):
#         rectangle += (make_line(size) * 3) + '\n'
#     return rectangle

# print(make_rectangle(5))

#My original solution to the rectangle question here was, I suppose,
#less elegant and less dynamic.  It made a rectangle, but couldn't
#accept arguments for both the height AND the width. 



# Part 2 A -- Make a Stairs

def make_stairs(height):
    stair = ''
    for i in range(height):
        stair += (make_line(i+1)) + '\n'
    return stair

print(make_stairs(5))


# def make_stairs(size):
#     stair = ''
#     for i in range(size):
#         stair += (make_line(size) * i) + '\n'
#     return stair

# print(make_stairs(5))

#My original sotluion, like the rectangle problem, seems to have WORKED
#but not been the exact solution the course designers were looking for.
#Is (make_line(i+1) any better / worse than (make_line(size) * i)?


# Part 2 B -- Make Space-Line 

def make_space_line(numSpaces, numChars):
    space_line = ' ' * numSpaces + '#' * numChars + ' ' * numSpaces
    return space_line

print(make_space_line(5, 5))

# Part 2 C -- Make Isosceles Triangle

def make_isosceles_triangle(height):
    triangle = ''
    for i in range(height):
        triangle += (make_space_line(height - i - 1, 2 * i +1) + '\n')
    return triangle

print(make_isosceles_triangle(5)) 

#I woudln't have figured this one out without the solution provided
#in the textbook... discouraging again... 

# Part 3 -- Make a Diamond

def make_diamond(height):
    triangle = ''
    inverted_triangle = ''
    for i in range(height):
        triangle += (make_space_line(height - i - 1, 2 * i +1) + '\n')
    for i in range(height, 0, -1):
       inverted_triangle += (make_space_line(height - i, 2 * i - 1) + '\n')
    return triangle + inverted

print(make_diamond(5)) 

#I'm somewhat proud that I came up with the idea that inverting the triangle
#is what I needed to do to get to a diamond shape.  However, I couldn't figure
#out how I needed to change the arguments in the inverted_triangle +=
#make_space_line() function, which I'm not as proud about.  I have to admit
#I don't really understand what's going on with (height, 0, -1) or "height - i,
#2 * i - 1").  I understand the solution provided in the textbook even less.  



