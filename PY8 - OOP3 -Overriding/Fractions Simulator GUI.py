#===============================================================
#Author: Eric Zhou
#Date: 12/12/2017
#Purpose: Test user's ability to perform fraction calculations
#Input: N/A
#Output: N/A
#===============================================================

import random
from tkinter import *

#===============================================================
#Author: Eric Zhou
#Date: 12/12/2017
#Purpose: To hold a fraction
#Input: N/A
#Output: N/A
#Methods =======================================================
#__init__:      - Constructs the fraction class.
#calcGCD:       - Finds the greatest common divisor.
#calcLCM:       - Finds the lowest common divisor of 2 numbers.
#reduce:        - Ensuring that denominator != 0, reduce fraction to lowest term.
#setValue:      - Sets the fraction with a numerator and denominator.
#randomize:     - Randomizes the fraction numerator and denominator +/-10.
#__str__:       - Returns fraction in proper mixed number form.
#calcInverse:   - Returns the inverse fraction of current fraction.
#__eq__:        - Returns true if a given fraction equals current fraction.
#__add__:       - Returns a fraction which is the result of adding a given fraction to current fraction.
#__sub__:       - Returns a fraction which is the result of subtracting a given fraction to current fraction.
#__mul__:       - Returns a fraction which is the result of multiplying a given fraction to current fraction.
#__div__:       - Returns a fraction which is the result of dividing a given fraction to current fraction.
#randomOperator:- Gets a random operator +, -, /, *
#===============================================================

class Fraction():
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        
#================================================================
#Date: Oct 13, 2017
#Author: Eric Zhou
#Purpose: Find the greatest common multiple of 2 positive Numbers
#Inputs: self, m, n
#Outputs: Return the greatest common divisor
#================================================================
        
    def calcGCD(self, m=0, n=1):
        if n == 0:
            n = 1
        t = m % n
        while t != 0:
            m = n
            n = t
            t = m % n
        return n
    
#================================================================
#Date: Oct 13, 2017
#Author: Eric Zhou
#Purpose: Find the least common divider of 2 positive Numbers
#Inputs: self, m, n
#Outputs: Return the least common multiple
#================================================================

    def calcLCM(self,m=0, n=1):
        GCD = self.calcGCD(m, n)
        LCM = m * n // GCD
        return LCM
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Reduces the numerator if it's greater than denominator.
#Inputs: self
#Outputs: None
#================================================================   
    def reduce(self):
        if self.denominator == 0:
            self.denominator = 1
            self.numerator = 0
            
        GCD = self.calcGCD(self.numerator, self.denominator)
        self.numerator //= GCD
        self.denominator //= GCD
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Sets the value of numerator and denominator
#Inputs: self, value1, value2
#Outputs: Return the least common multiple
#================================================================ 
    def setValue(self, val1 ,val2):
        self.numerator = val1
        self.denominator = val2
    
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Randomizes the numerator and denominator's values
#Inputs: self
#Outputs: Return the least common multiple
#================================================================ 
    def randomize(self):
        self.numerator = random.randint(-10, 10)
        self.denominator = random.randint(-10,10)
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Returns string form of fraction
#Inputs: self
#Outputs: Return the least common multiple
#================================================================ 
    def __str__(self):
        e = 0
        m = self.numerator
        n = self.denominator

        if m > 0:
            while m >= n and not n <= 0:
                m -= n
                e += 1
                
        elif m < 0:
            while m <= n * -1 and not n <= 0:
                m += n
                e -= 1

        if e < 0:
            m *= -1

        if e != 0 and m != 0:
            strFraction = str(e) + " " + str(m) + " / " + str(n)
        elif m != 0 and e == 0:
            strFraction = str(m) + " / " + str(n)
        else:
            strFraction = str(e)
            
        return strFraction
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Get's the inverse of a fraction.
#Inputs: self
#Outputs: Return the result of inverse
#================================================================ 
    def calcInverse(self):
        self.numerator, self.denominator = self.denominator, self.numerator
        return str(self.numerator) + "/" + str(self.denominator)
    
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Sees if fraction1 given fraction, fraction2
#Inputs: self, fraction
#Outputs: Return boolean validity
#================================================================ 
    def __eq__(self, fraction):
        f = fraction
        if self.denominator == f.denominator and self.numerator == f.numerator:
            equal = True
        else:
            equal = False

        return equal
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Adds two fractions together
#Inputs: self, fraction
#Outputs: Result of the sum of adding 2 fractions
#================================================================ 
    def __add__(self, fraction):
        f = fraction
        GCD = self.calcGCD(f.denominator)
        m = self.numerator
        n = self.denominator
        a = f.numerator
        b = f.denominator
        mul1 = 1
        mul2 = 1
        if n == b:
            ansNumerator = m + a
            ansDenominator = n
        else:
            LCM = self.calcLCM(self.denominator, fraction.denominator)
            if not self.denominator == LCM:
                mul1 = LCM // self.denominator
                
            if not fraction.denominator == LCM:
                mul2 = LCM // fraction.denominator
                
        m *= mul1
        n *= mul1
        a *= mul2
        b *= mul2          

        ansNumerator = m + a
        ansDenominator = n
        ans=Fraction(ansNumerator, ansDenominator)
        ans.reduce()
        storeNumerator.set(value=ans.numerator)
        storeDenominator.set(value=ans.denominator)

        return ans
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Subtract fraction2 with fraction1
#Inputs: self, fraction
#Outputs: Return the difference of the fractions
#================================================================ 
    def __sub__(self, fraction):
        f = fraction
        GCD = self.calcGCD(f.denominator)
        m = self.numerator
        n = self.denominator
        a = f.numerator
        b = f.denominator
        mul1 = 1
        mul2 = 1

        if n == b:
            ansNumerator = m - a
            ansDenominator = n

        else:
            LCM = self.calcLCM(self.denominator, fraction.denominator)
            if not self.denominator == LCM:
                mul1 = LCM // self.denominator

            if not fraction.denominator == LCM:
                mul2 = LCM // fraction.denominator

        m *= mul1
        n *= mul1
        a *= mul2
        b *= mul2          

        ansNumerator = m - a
        ansDenominator = n
        ans=Fraction(ansNumerator, ansDenominator)
        ans.reduce()
        storeNumerator.set(value=ans.numerator)
        storeDenominator.set(value=ans.denominator)
        return ans
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Multiplies fraction1 with fraction2
#Inputs: self, fraction
#Outputs: Return the product of the fractions
#================================================================ 
    def __mul__(self, fraction):
        f = fraction
        ansNumerator = self.numerator * f.numerator
        ansDenominator = self.denominator * f.denominator
        ans = Fraction(ansNumerator, ansDenominator)
        ans.reduce()
        storeNumerator.set(value=ans.numerator)
        storeDenominator.set(value=ans.denominator)
        return ans
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Multiplies fraction1 with fraction2
#Inputs: self, fraction
#Outputs: Return the result
#================================================================ 
    def __floordiv__(self, fraction):
        f = fraction
        f.calcInverse()
        ansNumerator = self.numerator * f.denominator
        ansDenominator = self.denominator * f.numerator
        ans = Fraction(ansNumerator, ansDenominator)
        ans.reduce()
        storeNumerator.set(value=ans.numerator)
        storeDenominator.set(value=ans.denominator)
        
        return ans
#================================================================
#Date: Dec 17, 2017
#Author: Eric Zhou
#Purpose: Gets a random operator
#Inputs: self
#Outputs: Returns the operator
#================================================================ 
    def randomOperator(self):
        getOp =random.randint(1,4)
        if getOp == 1:
            op = "+"
        if getOp == 2:
            op = "-"
        if getOp == 3:
            op = "*"
        if getOp == 4:
            op = "/"
        return op
    
#SUBPROGRAM
#================================================================
#Date: Dec 18, 2017
#Author: Eric Zhou
#Purpose: Runs the main program
#Inputs: None
#Outputs: None
#================================================================ 
def setup():
    frac1 = Fraction()
    frac2 = Fraction()

    frac1.randomize()
    frac2.randomize()
    frac1.reduce()
    frac2.reduce()

    op = frac1.randomOperator()
    if op == "+":
        answer = frac1.__add__(frac2)
    if op == "-":
        answer = frac1.__sub__(frac2)
    if op == "*":
        answer = frac1.__mul__(frac2)
    if op == "/":
        answer = frac1.__floordiv__(frac2)
    
    answer.reduce()
    genAnswer = random.randint(1,2)
    
    if genAnswer == 1:    
        equation.set(value=(frac1.__str__() + "  " + op + "  " + frac2.__str__() + " = " + answer.__str__()))
        
    if genAnswer == 2:
        answer.numerator += random.randint(-10,10)
        answer.denominator += random.randint(-10,10)
        equation.set(value=(frac1.__str__() + "  " + op + "  " + frac2.__str__() + " = " + answer.__str__()))
        
    otherDenominator.set(value=answer.denominator)
    otherNumerator.set(value=answer.numerator)
#================================================================
#Date: Dec 19, 2017
#Author: Eric Zhou
#Purpose: Checks to see if the display answer is the real answer
#Inputs: None
#Outputs: None
#================================================================     
def checkAns():
    ansNumerator = int(storeNumerator.get())
    ansDenominator = int(storeDenominator.get())
    
    disNumerator = int(otherNumerator.get())
    disDenominator = int(otherDenominator.get())
    
    totalTries = int(tries.get())
    totalWins = int(wins.get())

    strAns = str(answer.get())
    
    if strAns == "True" and (ansNumerator == disNumerator and ansDenominator == disDenominator):
        totalWins += 1
        totalTries += 1
        
    elif strAns == "False" and (ansNumerator != disNumerator and ansDenominator != disDenominator):
        totalTries += 1
        totalWins += 1
    else:
        totalTries += 1

    tries.set(value=totalTries)
    wins.set(value=totalWins)
    score.set(value="Score: " + str(wins.get()) + "/" + str(tries.get()))
#================================================================
#Date: Dec 21, 2017
#Author: Eric Zhou
#Purpose: Resets the score
#Inputs: None
#Outputs: None
#================================================================   
def reset():
    tries.set(value="0")
    wins.set(value="0")
    score.set(value="Score: " + str(wins.get()) + "/" + str(tries.get()))
    setup()
    
            
        
#=====================================================================================================
mainWindow = Tk()
mainWindow.title("Fractions Simulator")

#Menu
menubar = Menu(mainWindow)

#File Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="Exit",
                     command=lambda:(messagebox.showinfo("Bye!", "Good Bye, User!"),mainWindow.destroy()))
menubar.add_cascade(label="File", menu=filemenu)

#Edit Menu
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Edit", menu=editmenu)

#Help Menu
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="About",
                     command=lambda:messagebox.showinfo(" About ", " This program was created by Eric Zhou :) "))
menubar.add_cascade(label="Help", menu=helpmenu)        
    
            
#Main Window Config
mainWindow.config(menu=menubar, bg="white", width=300, height=250)

#StringVars
tries = StringVar()
tries.set(value=0)
wins = StringVar()
wins.set(value=0)
score = StringVar()
score.set(value="Score: " + str(wins.get()) + "/" + str(tries.get()))
equation = StringVar()
equation.set(value=" 0 + 0 = ? ")
storeNumerator = StringVar()
storeDenominator = StringVar()
otherDenominator = StringVar()
otherNumerator = StringVar()
answer = StringVar()
answer.set(value="False")

resetButton = Button(mainWindow, text="Reset", font=("Times bold", 11), bg="yellow", fg="black", relief = "solid", width=6, command=lambda:(reset()))
resetButton.place(x=30, y=205)
quitButton = Button(mainWindow, text="Quit", font=("Times bold", 11), bg="blue", fg="white", relief = "solid", width=6, command=lambda:(messagebox.showinfo("Bye!", "Good bye, User!"), mainWindow.destroy()))
quitButton.place(x=220, y=205)

rightButton = Button(mainWindow, highlightthickness=5, highlightbackground="black", text="Right!", font=("Times bold", 15), bg="green", fg="white", relief = "solid", height =3, width=10, command=lambda:(answer.set(value="True"), checkAns(), setup()))
rightButton.place(x=20, y= 100)
wrongButton = Button(mainWindow, highlightthickness=5, highlightbackground="black", text="Wrong!", font=("Times bold", 15), bg="maroon", fg="white", relief = "solid", height =3, width=10, command=lambda:(answer.set(value="False"), checkAns(), setup()))
wrongButton.place(x=155, y= 100)

displayEq = Label(mainWindow, textvariable = equation, font=("Times bold", 17), bg="lightskyblue", fg="blue", relief="solid")
displayEq.place(x=30, y=15)

scoreboard = Label(mainWindow, textvariable = score, font=("Times bold", 14), bg= "indianred1", fg="maroon", relief="solid")
scoreboard.place(x=102, y=60)

setup()
mainloop()
