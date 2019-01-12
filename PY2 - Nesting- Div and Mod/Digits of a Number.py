#Author: Eric Zhou
#Date: September 28, 2017
#Purpose: To find sum of digits, number of digits and the reversal number
#input: keyboard
#Output: screen/console
#===========================================================

number = -1
while not number >0:
    number = int(input("Enter a number!: "))
    
palindrome_number = number
digitSum = 0
digit = 0
digit_number = number
digitalRoot =0

while digit_number >0:
    digitSum += digit_number %10
    digit_number //= 10
    digit += 1
    
print("There are", digit, "digits")
print("The sum of the digits are", digitSum)

while digitSum >0:
    digitalRoot += digitSum %10
    digitSum //= 10

attempts = 0
totalDigitalRoot = 0   
while (digitalRoot >0 or digitalRoot not in range(0,10) and attempts <20):
    totalDigitalRoot += digitalRoot %10
    digitalRoot //= 10
    attempts += 1
print("The digital root of the sum of the number is", totalDigitalRoot)


reverse_number = 0
while number >0:
    print(number)
    remainder = number %10
    reverse_number = (reverse_number *10) + remainder
    number //= 10

if palindrome_number == reverse_number:
    print("The number you entered", palindrome_number, "is a palindrome.")
else:
    print("The reverse of the number is", reverse_number)
