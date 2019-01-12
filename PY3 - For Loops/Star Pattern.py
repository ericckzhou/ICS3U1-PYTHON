#Author: Eric Zhou
#Date: Oct 7, 2017
#Purpose: Generating shapes with star patterns
#Input: Keyboard
#Outputs: Screen/Console
#==================================================

print("Please choose the following star patterns and enter a size between 1 - 20:")
print("Select the shape you desire!: ")
print("a = Square")
print("b = Hollow Square")
print("c = Triangle")
print("d = Hollow Triangle")
print("e = Diamond")
print("f = Hollow Diamond")

shape = 0
size = 0
count = 0
stars = ""
hollow = ""
sizeCount = 0

#Shape and Size determination
while not (shape == 'a' or shape == 'b' or shape == 'c' or shape == 'd' or shape == 'e' or shape == 'f'):
    shape = input("Please enter the letter of the shape you desire: ")

if (shape == 'e' or shape == 'f'):
    while not (size > 0 and size <= 20 and size % 2 == 1):
        size = int( input("Please enter the size of your shape (must be odd for this shape): "))
else:
    while not (size > 0 and size <= 20):
        size = int( input("Please enter the size of your shape: "))

# Square
if (shape == 'a'):
    star = '* '
    while sizeCount != size:
        for count in range(size):
            print(star, end= "")
        print("")
        sizeCount += 1
  
# Hollow Square  
elif (shape == 'b'):
    stars = "* "
    hollow = "  "
    for count in range(1, size + 1):
        print(stars, end = "")
    print("")
    for count in range(1, size - 1):
        print(stars, end = "")
        for count in range(1, size - 1):
            print(hollow, end = "")
        print(stars)
    for count in range(1, size + 1):
        print(stars, end = "")

# Triangle  
elif (shape == 'c'):
    while sizeCount != size:
        star = '* '
        
        for count in range(sizeCount +1):
            print(star, end = "")
        print("")
        sizeCount += 1

# Hollow Triangle
elif (shape == 'd'):
    stars = "* "
    hollow = "  "
    
    if (size == 1 or size == 2):
        for count in range(1, size + 1):
            for count in range(1, count + 1):
                print(stars, end = "")
            print("")
            
    elif (size > 2):
        for count in range(1, 3):
            for count in range(1, count + 1):
                print(stars, end = "")
            print("")
            
        for count in range(1, size - 2):
            print(stars, end = "")
            for count in range(1, count + 1):
                print(hollow, end = "")
            print(stars)
            
        for count in range(1, size + 1):
            print(stars, end = "")

# Diamond
elif (shape == 'e'):
    for count in range(size//2):
        print((size//2 - count) * "  " + (2 * count + 1) * "* ")
        
    for count in range(size//2, -1, -1):
        print((size//2 - count) * "  " + (2 * count + 1) * "* ")

# Cross
elif (shape == 'f'):
    for count in range(size//2):
        if not count == 0:
            print((size//2 - count) * "  " + "* " + (2 * count - 1) * "  " + "* ")
        else:
            print((size//2 - count) * "  " + "* " + (2 * count - 1) * "  ")
            
    for count in range(size//2, -1, -1):
        if not count == 0:
            print((size//2 - count) * "  " + "* " + (2 * count - 1) * "  " + "* ")
        else:
            print((size//2 - count) * "  " + "* " + (2 * count - 1) * "  ")


