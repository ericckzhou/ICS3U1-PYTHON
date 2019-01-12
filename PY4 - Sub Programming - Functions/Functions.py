#Date: Oct 11, 2017
#Author: Eric Zhou
#Purpose: Obtaining POSITIVE integers and return a valid positive integer number within the range
#Inputs: Keyboard and a prompt parameter with entered range
#Outputs: Positive Number being returned.
#================================================================================================
print('1 = getPositiveInteger ')
print('2 = calcFactorial ')
print('3 = calcPermutations ')
print('4 = calcCombinations ')
print('5 = calcGCD ')
print('6 = calcLCM ')
print('7 = isRelativelyPrime' )
print('8 = "Simple Program" ')

program = input("Enter a Program Number: ")
while not (program == '1' or program == '2' or program == '3' or program == '4' or program == '6' or program == '5' or program == '7' or program == '8'):
    print("The last input was not an  in range 1-8! ")
    program = input("Enter a Program Number: ")
    lastInput = program

import random

#Author: Eric Zhou
#Date: Oct 12, 2017
#Purpose: Gets a valid and positive integer from user
#Inputs: Keyboard, integer
#Outputs: Returns integer of user input
def getPositiveInteger(prompt="Enter a positive integer number : ", low = 0 , high = 100):
    intUserInput = low -1
    while (intUserInput < low or intUserInput > high):
        strUserInput = ""
        while (not strUserInput.isdigit()):
            strUserInput = input(prompt + " with a value between " + str(low) + " and " + str(high) + ': ')
            if (not strUserInput.isdigit()):
                print("ATTENTION: Your last input was not a valid positive integer; please try again.  ")
        intUserInput = int(strUserInput)
        if (intUserInput < low or intUserInput > high):
            print("ATTENTION: Your last input was not in the range of " + str(low) + " and " + str(high) + ': ')
    return intUserInput

if program == '1':
    #MAIN CODE
    lowest = getPositiveInteger()
    largest = getPositiveInteger()
    if lowest > largest:
        randomNumber = random.randint(largest, lowest)
        print("The random valid number chosen within the range,", str(largest),"-", str(lowest), "is", str(randomNumber))
    else:
        randomNumber = random.randint(lowest, largest)
        print("The random valid number chosen within the range,", str(lowest),"-", str(largest), "is", str(randomNumber))

#==================================
#Date: Oct 12, 2017
#Author: Eric Zhou
#Purpose: Find the factorial of n
#Inputs: Keyboard and factorial
#Outputs: Return factorial
#==================================

def getFactorial(number=0):
    factorialNumber = 1
    total = 1
    while factorialNumber != (number +1):
        total *= (factorialNumber + number) - number
        factorialNumber += 1
    return total

#MAIN CODE
if program == '2':
    number = getPositiveInteger()
    calcFactorial = getFactorial(number)
    print("The factorial is " + str(round(calcFactorial,3)))

#==============================================
#Date: Oct 12, 2017
#Author: Eric Zhou
#Purpose: Use the formula to receive an output
#Inputs: Keyboard and 2 numbers
#Outputs: Return the permutation of the 2 numbers
#==============================================

#MAIN CODE
if program == '3':
    n = getPositiveInteger()
    r = getPositiveInteger()
    m = 0

    if n < r:
        m = r - n
        m = getFactorial(number)
        r = getFactorial(r)
        n = getFactorial(n)
        calcPermutations = r / (m)
    else:
        m = n - r
        m = getFactorial(n-r)
        r = getFactorial(r)
        n = getFactorial(n)
        calcPermutations = n / (m)

    print("The permutation is " + str(round(calcPermutations,3)))

#================================================
#Date: Oct 13, 2017
#Author: Eric Zhou
#Purpose: Finding the combinations of 2 numbers
#Inputs: Keyboard, n and r
#Outputs: Return the combinations of the 2 numbers
#================================================

#MAIN CODE
if program == '4':
    n = getPositiveInteger()
    r = getPositiveInteger()
    m = 0

    if n < r:
        m = r - n
        m = getFactorial(r-n)
        r = getFactorial(r)
        n = getFactorial(n)
        calcCombinations = r / (n * (m))
    else:
        m = n - r
        m = getFactorial(n-r)
        r = getFactorial(r)
        n = getFactorial(n)
        calcCombinations = n / (r * (m))
    print("The combinations entered produced " + str(round(calcCombinations,3)))

#================================================================
#Date: Oct 13, 2017
#Author: Eric Zhou
#Purpose: Find the greatest common divisor of 2 positive Numbers
#Inputs: Keyboard, 2 positive integers
#Outputs: Return the greatest common divisor
#================================================================

def calcGCD(m, n):
    t = m % n
    while t != 0:
        m = n
        n = t
        t = m % n
    return n

#MAIN CODE
if program == '5':
    m = getPositiveInteger()
    n = getPositiveInteger()

    calcGCD = calcGCD(m, n)
    print("The greatest common divisor of " + str(m) + ' , ' + str(n) + ' is ' + str(calcGCD))

#================================================================
#Date: Oct 13, 2017
#Author: Eric Zhou
#Purpose: Find the least common multiple of 2 positive Numbers
#Inputs: Keyboard, 2 positive integers
#Outputs: Return the least common multiple
#================================================================

def calcLCM(m, n, GCD):
    LCM = m * n / GCD
    return LCM

#MAIN CODE
if program == '6':
    m = getPositiveInteger()
    n = getPositiveInteger()
    GCD = calcGCD(m, n)

    LCM = calcLCM(m, n, GCD)
    print("The lowest common multiple of " + str(m) + ' , ' + str(n) + ' is ' + str(LCM))

#================================================================
#Date: Oct 13, 2017
#Author: Eric Zhou
#Purpose: Find out if the given 2 numbers are relatively prime
#Inputs: Keyboard, 2 positive integers
#Outputs: Return the GCD if it equals to 1 or not
#================================================================

#MAIN CODE
if program == '7':
    m = getPositiveInteger()
    n = getPositiveInteger()
    GCD = calcGCD(m, n)
    
    if GCD == 1:
        print("The values of " + str(m) + " and " + str(n) + " produce a relatively prime result. ")
    else:
        print("The values of " + str(m) + " and " + str(n) + " did not produce a relatively prime result. ")
          
#=======================================================================================================================
#Date: Oct 13, 2017
#Author: Eric Zhou
#Purpose: Finding the LCM, GCD, combinations, permutations and if its relatively prime of the given 2 positive integers
#Inputs: Keyboard, 2 positive integers
#Outputs: Return the LCM, GCD, combinations, permutations and if its relatively prime of the given 2 positive integers
#========================================================================================================================

def simple_program():
    m = getPositiveInteger()
    n = getPositiveInteger()
    GCD = calcGCD(m, n)
    LCM = calcLCM(m, n, GCD)
    
    if n < m or n == m:
        f = getFactorial(m-n)
        m = getFactorial(m)
        n = getFactorial(n)
        calcCombinations = m / (n * (f))
        calcPermutations = m / (f)
    elif m < n:
        f = getFactorial(n-m)
        m = getFactorial(m)
        n = getFactorial(n)
        calcCombinations = n / (m * (f))
        calcPermutations = n / (f)
        
        
    if GCD == 1: 
        return print("The given 2 positive integers produced ; permutations = " + str(round(calcPermutations,3)) + ' combinations of ' + str(round(calcCombinations,3)) + ' \
GCD = ' + str(round(GCD,3)) + ' LCM = ' + str(round(LCM,3)) + ' and the 2 given numbers produce a relatively prime result. ')
    
    if GCD != 1:
        return print("The given 2 positive integers produced ; permutations = " + str(round(calcPermutations,3)) + ' combinations of ' + str(round(calcCombinations,3)) + ' \
GCD = ' + str(round(GCD,3)) + ' LCM = ' + str(round(LCM,3)) + ' and the 2 given numbers did not produce relatively prime result. ')
       
    
#MAIN CODE
rerun = False
if program == '8':
    simple_program()

    while rerun == False:
        userInput = input("Would you like to run the program again? Y/N ")
        if userInput == 'y' or userInput == 'Y':
            simple_program()
        if userInput == 'n' or userInput == 'N':
            quit()
        if userInput != 'y' or userInput != 'n' or userInput != 'N' or userInput != 'Y':
            print("Choose Y or N only! ")








