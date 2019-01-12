#Author: Eric Zhou
#Date: September 31, 2017
#Purpose: Making user input -9999 number but it cannot be the first number it enters
#Input: Keyboard
#Output: Screen/console
#===========================================================

number = int(input("Enter a number!: "))

if number != -9999:
    largestNumber = number
    smallestNumber = number
    totalSum = number
    guess = 1
    
else:
    guess =0
    totalSum = 0
    largestNumber = 0
    smallestNumber = 0
    
while number != -9999 or guess <1:
    number = int(input("Enter a number!: "))
    
    if number != -9999:
        guess += 1
        totalSum += number
        
    if smallestNumber <=0 and guess in range(0,2):
        smallestNumber = largestNumber
        
    if largestNumber < number and number != -9999:
         largestNumber = (largestNumber - largestNumber) + number

    if smallestNumber > number and number != -9999:
        smallestNumber = (smallestNumber - smallestNumber) + number
        
print("The largest number is", largestNumber)
print("The smallest number is", smallestNumber)
print("The average number is", round(totalSum / guess,2))


