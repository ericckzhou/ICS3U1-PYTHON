#Date: Sept 19, 2017
#Author: Eric Zhou
#Purpose: Completing series program
#Inputs: Keyboard
#Output: Screen/Console
#============================================

#Series #1
number = 1
times = 1
while times <=20:
    number = number * times
    print(number)
    times = times +1

#Series #2

answerA = 0
sumA = 0
countA = 0
denominator = 1
sign = False
while countA < 1000000:
    if sign == False:
        sumA = sumA + 1/denominator
        denominator = denominator + 2
        countA = countA + 1
        sign = True
    else:
        sumA = sumA - 1/denominator
        denominator = denominator + 2
        countA = countA + 1
        sign = False

answerA = 4 * sumA
print(answerA)

#Series 3
denominatorA = 3
countA = 0
sumB = 0
numerator = 1
while not countA == 1000000:
    sumB = sumB + 1/(numerator*denominatorA)
    countA = countA +1
    numerator = numerator +2
    denominatorA = denominatorA +2

print(sumB)
    
