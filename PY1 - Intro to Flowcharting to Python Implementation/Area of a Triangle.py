#Date: September 19, 2017
#Author: Eric Zhou
#Purpose: Finding the Area of a Triangle
#Inputs: Keyboard
#Output: Console/screen
#===========================================================

import math

sideA = -1
sideB = -1
sideC = -1

while not (sideA + sideB > sideC and sideB + sideA > sideC and sideC + sideB > sideA):
       while (sideA<0):
           sideA = float(input("Please enter the first side of the triangle : "))

       while (sideB<0):
           sideB = float(input("Please enter the second side of the triangle : "))

       while (sideC<0):
           sideC = float(input("Please enter the third side of the triangle : "))

semiPerimeter = 0.5*(sideA + sideB + sideC)
area = math.sqrt(semiPerimeter * (semiPerimeter - sideA)*(semiPerimeter - sideB)*(semiPerimeter - sideC))
print("The area of the triangle is", round(area, 3), "units squared")
