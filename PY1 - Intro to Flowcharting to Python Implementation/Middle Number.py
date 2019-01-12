#Date: Sept 19, 2017
#Author: Eric Zhou
#Purpose: To find the middle number of 3 numbers.
#Inputs: keyboard
#Output: Screen/Console
#=================================

num1 = -1
num2 = -1
num3 = -1

while num1 <0 and num2 <0 and num3 <0:

    num1 = -1
    while num1 <0 or num1 %2 != 0:
        num1 = float(input("Enter the first number: "))

    num2 = -1
    while num2 <0 or num2 == num1 or num2 %2 != 0:
        num2 = float(input("Enter the second number: "))

    num3 = -1
    while num3 <0 or num1 == num3 or num3 == num2 or num3 %2 != 0:
        num3 = float(input("Enter the third number: "))
         
if num1 > num2 and num1 < num3 or num1 < num2 and num1 > num3:
    print("You have chosen the number",(num1, num2, num3), "and the Middle Number is", num1)
    
if num2 > num1 and num2 < num3 or num2 < num1 and num2 > num3:
    print("You have chosen the number",(num1, num2, num3), "and the Middle Number is", num2)
    
if num3 > num1 and num3 < num2 or num3 < num1 and num3 > num2:
    print("You have chosen the numbers",(num1, num2, num3), "and the Middle Number is", num3)

