#===============================================================
#Author: Eric Zhou
#Date: Oct 25, 2017
#Purpose: To create a GUI verson of Number Theory
#Inputs: Keyboard, 2 valid positive numbers, click "proceed"
#Outputs: Screen, returns factorials of two numbers,
#the permutations, combinations, GCD, LCM and if the two numbers
#entered are relatively prime.
#===============================================================

from tkinter import *

#==================================
#Date: Oct 12, 2017
#Author: Eric Zhou
#Purpose: Find the factorial of n
#Inputs: Keyboard and factorial
#Outputs: Return factorial
#==================================

def getFactorial(number=0):
    factorialNumber = 0
    total = 1
    while factorialNumber != (number):
        factorialNumber += 1
        total *= (factorialNumber + number) - number
    return total

#==============================================
#Date: Oct 12, 2017
#Author: Eric Zhou
#Purpose: Use the formula to receive an output
#Inputs: Keyboard and 2 numbers
#Outputs: Return the permutation of the 2 numbers
#==============================================

def calcPermutations(n, r):
    m = 0

    if n < r:
        m = r - n
        m = getFactorial(r-n)
        r = getFactorial(r)
        n = getFactorial(n)
        calcPermutations = r / (m)
    else:
        m = n - r
        m = getFactorial(n-r)
        r = getFactorial(r)
        n = getFactorial(n)
        calcPermutations = n / (m)
    return calcPermutations

#================================================
#Date: Oct 13, 2017
#Author: Eric Zhou
#Purpose: Finding the combinations of 2 numbers
#Inputs: Keyboard, n and r
#Outputs: Return the combinations of the 2 numbers
#================================================

def calcCombinations(n, r):
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
        
    return calcCombinations

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

#================================================================
#Date: Oct 13, 2017
#Author: Eric Zhou
#Purpose: Find out if the given 2 numbers are relatively prime
#Inputs: Keyboard, 2 positive integers
#Outputs: Return the GCD if it equals to 1 or not
#================================================================

def getRelativelyPrime(GCD):
    if GCD == 1:
        relativelyPrime = "relatively prime "
    else:
        relativelyPrime = "not relatively prime "
    return relativelyPrime

#================================================================
#Date: Oct 26, 2017
#Author: Eric Zhou
#Purpose: Main code subprogram, sees if numbers entered are valid
#Inputs: Keyboard,
#Outputs: GUI statements, errors
#================================================================

def buttonPressed():
    valid = True
    strNumber1 = str(firstNumber.get())
    strNumber2 = str(secondNumber.get())
    if not (strNumber1.isdigit() and strNumber2.isdigit()):
        messagebox.showerror("Error", "Your last inputs were not all valid positive integers. ")
        valid = False
        
    if valid == True:
        number1 = int(firstNumber.get())
        number2 = int(secondNumber.get())
        if not(number1 >0 and number2 >0 and number1 <=10 and number2 <=10):
            messagebox.showerror("Error", "Your last inputs were not in range 1-10. ")
            valid = False
        
    if valid == True:
        valFirst = getFactorial(number1)
        factorial1.set(value = " The factorial of the first number is " + str(valFirst))
        valSecond = getFactorial(number2)
        factorial2.set(value = " The factorial of the second number is " + str(valSecond))
        valPermutations = calcPermutations(number1, number2)
        permutations.set(value = " The permutations is " + str(valPermutations))
        valCombinations = calcCombinations(number1, number2)
        combinations.set(value = " The combinations is " + str(valCombinations))
        valGCD = calcGCD(number1, number2)
        GCD.set(value = " The GCD is " + str(valGCD))
        valLCM = calcLCM(number1, number2, valGCD)
        LCM.set(value = " The LCM is " + str(valLCM))
        valRelativelyPrime = getRelativelyPrime(valGCD)
        relativelyPrime.set(value = "The two numbers entered is " + str(valRelativelyPrime))

#MAIN WINDOW
mainWindow = Tk()
mainWindow.title("Number Theory")

#Menu
menubar = Menu(mainWindow)

#File Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open",
                     command=lambda:messagebox.showerror("Error", "Not completed"))
filemenu.add_command(label="Save",
                     command=lambda:messagebox.showerror("Error", "Not completed"))
filemenu.add_separator()
filemenu.add_command(label="Exit",
                     command=lambda:mainWindow.destroy())
menubar.add_cascade(label="File", menu=filemenu)

#Edit Menu
editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label="Cut",
                     command=lambda:messagebox.showerror("Error", "Not completed"))
editmenu.add_command(label="Copy",
                     command=lambda:messagebox.showerror("Error", "Not completed"))
editmenu.add_command(label="Paste",
                     command=lambda:messagebox.showerror("Error", "Not completed"))
editmenu.add_command(label="Redo",
                     command=lambda:messagebox.showerror("Error", "Not completed"))
menubar.add_cascade(label="Edit", menu=editmenu)

#Help Menu
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="About",
                     command=lambda:messagebox.showinfo(" About ", " This program was created by Eric Zhou :) "))
menubar.add_cascade(label="Help", menu=helpmenu)

#Frames (Gray/Blue)
Frame(bg = "gray", width = 300, height = 125).place(x=0, y=0)
Frame(bg = "white", width= 275, height =100).place(x=13, y=13)
Frame(bg = "steelblue", width = 300, height=225).place(x=0, y=125)
Frame(bg = "white", width = 275, height = 195).place(x=13, y=140)

mainWindow.config(menu=menubar, width= 300, height = 350)

#StringVars
factorial1 = StringVar()
factorial1.set(value="")
factorial2 = StringVar()
factorial2.set(value="")
firstNumber = StringVar()
firstNumber.set(value = "")
secondNumber = StringVar()
secondNumber.set(value = "")
number = StringVar()
number.set(value = "")
permutations = StringVar()
permutations.set(value = "")
combinations = StringVar()
combinations.set(value = "")
GCD = StringVar()
GCD.set(value = "")
LCM = StringVar()
LCM.set(value = "")
relativelyPrime = StringVar()
relativelyPrime.set(value = "")

#Gray Box
Label(mainWindow, text = ' Enter the first number: ').place(x= 15, y=25)
Entry(mainWindow, textvariable = firstNumber).place(x=160, y = 25)
Label(mainWindow, text = ' Enter the second number: ').place(x= 15, y=50)
Entry(mainWindow, textvariable = secondNumber).place(x=160, y = 50)
Button(mainWindow, text= " Proceed ", command=lambda:buttonPressed()).place(x=110, y=85)

#Steel-Blue Box
Label(mainWindow, textvariable = factorial1).place(x=13, y = 150)
Label(mainWindow, textvariable = factorial2).place(x=13, y = 175)
Label(mainWindow, textvariable = permutations).place(x=13, y=200)
Label(mainWindow, textvariable = combinations).place(x=13, y=225)                    
Label(mainWindow, textvariable = GCD).place(x=13, y=250)
Label(mainWindow, textvariable = LCM).place(x=13, y=275)
Label(mainWindow, textvariable = relativelyPrime).place(x=13, y=300)

#Main Loop
mainloop()






