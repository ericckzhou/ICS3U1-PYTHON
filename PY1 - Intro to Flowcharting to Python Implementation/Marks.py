#Author: Eric Zhou
#Date: Sept 19, 2017
#Purpose: Marks
#Inputs: Keyboard
#Output: Screen/Console
#===========================

mark = int(input("What is your mark? "))
while mark >100 or mark <0:
    print("Enter an invalid mark please! ")
    mark = int(input("What is your mark? "))
    
if mark in range(0, 39):
    print("Fail")
elif mark in range(40, 49):
    print("Credit Recovery")
elif mark in range(50, 59):
    print("Level 1")
elif mark in range(60, 69):
    print('Level 2')
elif mark in range(70, 79):
    print('Level 3')
elif mark in range(80, 100):
    print('Level 4!')
