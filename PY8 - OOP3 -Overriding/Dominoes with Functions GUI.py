#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: To create dominos game
#Inputs: Keyboard
#Outputs: Screen
#====================================================

import random
from tkinter import *

#Orientation = Vertical(True) or Horizontal(False)
#Face Up = Face Up(True)/Down(False)

#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Creating Dominoes Class
#Inputs: value, size
#Outputs: None
#Methods ============================================
#__init__:       - constructs the Domino class.
#__str__:        - returns value of dominoes as a string.
#getValue:       - validates the value of the dominoes
#setValue:       - sets the value of the dominoes.
#flip:           - switches the value of the dominoes.
#setOrientation: - sets the orientation of the dominoes. Vertical(True) or Horizontal(False)
#setFace:        - sets the face of the domino Face Up(True)/Down(False)
#setSize:        - sets the size of the dominoes
#randomize:      - randomizes the value of dominoes
#draw:           - draws the domino's shape.
#drawDots:       - draw the dots of the dominoes.
#__add__:        - adds the value of 2 dominoes given
#__sub__:        - subtracts the value of 2 dominoes given
#__mul__:        - multiply the value of 2 dominoes given
#__gt__:         - determines if self.value is greater than domino value entered
#__lt__:         - determines if self.value is less than domino value entered
#__gtet__:       - determines if self.value is greater than equal to domino value entered
#__ltet__:       - determines if self.value is less than equal to domino value entered
#__eq__:         - determines if self.value equals to domino value entered
#__ne__:         - determines if self.value does not equal to domino value entered
#====================================================

class Domino():
    def __init__(self, value =0, size=30, diameter = 0, gap = 0, orientation = True, face = False):
        #value of domino
        self.value = value
        #size of domino
        self.size = size
        if not self.size in range(0, 101):
            self.size = 30
        #the diameter of domino
        self.diameter = size / 5
        #the gap between dots in dominos
        self.gap = diameter / 2
        #the orientation of the domino
        self.orientation = orientation
        if not (self.orientation == True or self.orientation == False):
            self.orientation = True
        #the face of the domino
        self.face = face
        if not (self.face == True or self.face == False):
            self.face = False
        
#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Return value of dominoes as a string
#Inputs: Self
#Outputs: None
#====================================================
        
    def __str__(self):
        self.value = int(sValue.get())
        return str(self.value)
        
#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Getting a valid value from user
#Inputs: Self
#Outputs: Return Valid value / error messages
#====================================================
    def getValue(self, x=0):
        valid = True
        if x == 0:
            if not (str(sValue.get()).isdigit()):
                valid = False
                messagebox.showerror("Error", "Your last value input was not a positive valid integer! ")

            if valid == True:  
                if not int(sValue.get()) in range(0,100):
                    valid = False
                    messagebox.showerror("Error", "Your last value input was not in range 0-99! ")
                if not (int(sValue.get()) // 10 in range(0,10) and int(sValue.get()) % 10 in range(0,10)) and valid == True:
                    valid = False
                    messagebox.showerror("Error", "Your last value input ones or tens digit was not in range 0-9! ")
        if x == 1:
            if not (str(sValue2.get()).isdigit()):
                valid = False
                messagebox.showerror("Error", "Your last value input was not a positive valid integer! ")

            if valid == True:  
                if not int(sValue2.get()) in range(0,100):
                    valid = False
                    messagebox.showerror("Error", "Your last value input was not in range 0-99! ")
                if not (int(sValue2.get()) // 10 in range(0,10) and int(sValue2.get()) % 10 in range(0,10)) and valid == True:
                    valid = False
                    messagebox.showerror("Error", "Your last value input ones or tens digit was not in range 0-9! ")
                
        return valid
    
#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Setting the value of dominoes
#Inputs: Self
#Outputs: None
#====================================================
    
    def setValue(self):
        self.value = int(sValue.get())
        
#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Set new flip value
#Inputs: Self
#Outputs: None
#====================================================
    def flip(self):
        value1 = self.value // 10
        value2 = self.value % 10
        value1, value2 = value2, value1
        self.value = value1 * 10 + value2
        
#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Sets orientation value
#Inputs: Self
#Outputs: None
#====================================================
    def setOrientation(self):
        if int(sOrientation.get()) == 1:
            self.orientation = True
        else:
            self.orientation = False
 #====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Sets face value
#Inputs: Self
#Outputs: None
#====================================================   
    def setFace(self):
        if int(sFace.get()) == 1:
            self.face = True
        else:
            self.face = False
#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Sets size value
#Inputs: Self
#Outputs: None
#====================================================
            
    def setGUISize(self):
        self.size = int(sizeScale.get())
        self.diameter = self.size // 5
        self.gap = self.diameter // 2
        
#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Sets size value
#Inputs: Self
#Outputs: None
#====================================================
            
    def setSize(self, size):
        if not size in range(30, 101):
            size = 30
        self.size = size
        self.diameter = self.size // 5
        self.gap = self.diameter // 2
#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Get random value
#Inputs: Self
#Outputs: Value
#====================================================
        
    def randomize(self):
        self.value = random.randint(0,99)

        return self.value

#====================================================
#Author: Eric Zhou
#Date: 11/15/2017
#Purpose: Draws the square of the dominoes
#Inputs: Self
#Outputs: None
#====================================================            
    def draw(self, canvas, domino2, x=0, y=0):
        x = str(getX.get())
        y = str(getY.get())
        
        if (not x.isdigit() or not y.isdigit()):
            getX.set(value=0)
            getY.set(value=0)
            x=0
            y=0

        x = int(x)
        y = int(y)
        if x > 99 or y > 99 or x <0 or y <0:
            getX.set(value=0)
            getY.set(value=0)
            x=0
            y=0
        
        canvas.delete("all")
        getColor = str(color.get())
        canvas.create_rectangle(self.size +x, self.size*2 +y, self.size *2 +x, self.size*3+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size +x,self.size+y, self.size *2+x, self.size *2+y, width=4, fill=getColor, outline="gray")
        
        canvas.create_rectangle(self.size*3 +x, self.size*2+y, self.size *4+x, self.size*3+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*3 +x, self.size+y, self.size *4+x, self.size *2+y, width=4, fill=getColor, outline="gray")
         
        canvas.create_rectangle(self.size*5 +x, self.size*2+y, self.size *6+x, self.size*3+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*5 +x, self.size+y, self.size *6+x, self.size *2+y, width=4, fill=getColor, outline="gray")

        
        dot1 = 0 #Top
        dot2 = 0 #Bottom
        
        if self.value <=9:
            dot1 = 0
            dot2 = self.value

        if self.value > 10:
            dot1 = self.value // 10
            dot2 = self.value % 10

        self.face = False
        self.orientation = True
        self.drawDots(c, dot1, 0 , 0, 0, 0)
        self.drawDots(c, dot2, 0 , 1, 0, 1)

        dot3 = domino2.value // 10
        dot4 = domino2.value % 10
        self.drawDots(c, dot3, 2, 0, 2, 0)
        self.drawDots(c, dot4, 2, 1, 2, 1)

        op = int(operator.get())
        if op == 1:
            ans = self.__add__(domino2)
        if op == 2:
            ans = self.__sub__(domino2)
        if op == 3:
            ans = self.__mul__(domino2)

        resultDomino.set(value=ans.value)
        
        domino3 = ans.value
        
        if domino3 > 99 or domino3 < 0:
            dot5 = 0
            dot6 = 0
        else:
            dot5 = domino3 // 10
            dot6 = domino3 % 10
    
            
        self.drawDots(c, dot5, 4, 0, 4, 0)
        self.drawDots(c, dot6, 4, 1, 4, 1)

        self.face = False
        self.orientation = False

#====================================================
#Author: Eric Zhou
#Date: 11/15/2017
#Purpose: Draw the dots of the dominoes
#Inputs: Self
#Outputs: None
#====================================================
        
    def drawDots(self, canvas, Dots, x1, y1, x2, y2):
        # # # # # #
        # o  o  o #
        # o  o  o #
        # o  o  o #
        # # # # # #
        #first row uses gap1
        #second row uses gap2
        #third row uses gap 3
        
        x = int(getX.get())
        y = int(getY.get())
        
        gap1 = self.gap + self.size 
        gap2 = (self.gap * 2) + (self.diameter) + self.size 
        gap3 = (self.gap * 3) + (self.diameter * 2) + self.size 
        
        dot = 0
        hDot = 0
        
        gapx1 = (x1 * self.size) +x
        gapx2 = (x2 * self.size) +x
        gapy1 = (y1 * self.size) +y
        gapy2 = (y2 * self.size) +y

        valid = True
        
        if self.face == False and self.orientation == True:
            dot = Dots #regular dots
            valid = True
            
        elif self.face == True and self.orientation == False:
            hDot = Dots #horizontal switched dots
            valid = True
            
        elif self.face == False and self.orientation == True:
            dot = Dots #same as regular dots
            valid = True

        if valid == True:
            if dot == 1 or hDot == 1:
                canvas.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")

            if dot == 2:
                canvas.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if hDot ==2:
                canvas.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")

            if dot == 3:
                canvas.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if hDot == 3:
                canvas.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")


            if dot == 4 or hDot == 4:
                canvas.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if dot == 5 or hDot == 5:
                canvas.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if dot == 6:
                canvas.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap2 + gapy1, gap1 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap2 + gapy1, gap3 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if hDot == 6:
                canvas.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap1 + gapy1, gap2 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap3 + gapy1, gap2 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
            if dot == 7:
                canvas.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap2 + gapy1, gap1 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")   
                canvas.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap2 + gapy1, gap3 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if hDot == 7:
                canvas.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap1 + gapy1, gap2 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap3 + gapy1, gap2 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                
            if dot == 8 or hDot == 8:
                canvas.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap2 + gapy1, gap1 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap2 + gapy1, gap3 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap1 + gapy1, gap2 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap3 + gapy1, gap2 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                
            if dot == 9 or hDot == 9:
                #COLUMN 1
                canvas.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap2 + gapy1, gap1 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                #COLUMN 2
                canvas.create_oval(gap2 + gapx1, gap1 + gapy1, gap2 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap2 + gapx1, gap3 + gapy1, gap2 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                #COLUMN 3
                canvas.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap2 + gapy1, gap3 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                canvas.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

#====================================================
#Author: Eric Zhou
#Date: 12/13/2017
#Purpose: Adds the 2 dominoes
#Inputs: Self, Domino
#Outputs: Result
#====================================================
    def __add__(self, domino):
        a = self.value // 10
        b = self.value % 10
        if a > b:
            domino1 = b * 10 + a
        else:
            domino1 = self.value

        x = domino.value // 10
        y = domino.value % 10
        if x > y:
            domino2 = y * 10 + x

        else:
            domino2 = domino.value

        ans = domino1 + domino2
        answer = Domino(ans, self.size, self.diameter, self.gap)

        return answer
#====================================================
#Author: Eric Zhou
#Date: 12/13/2017
#Purpose: Subtracts the 2 dominoes
#Inputs: Self, Domino
#Outputs: Result
#====================================================    
    def __sub__(self, domino):
        a = self.value // 10
        b = self.value % 10
        if a > b:
            domino1 = b * 10 + a
        else:
            domino1 = self.value

        x = domino.value // 10
        y = domino.value % 10
        
        if x > y:
            domino2 = y * 10 + x
        else:
            domino2 = domino.value
            
        ans = domino1 - domino2

        answer = Domino(ans, self.size, self.diameter, self.gap)

        return answer
#====================================================
#Author: Eric Zhou
#Date: 12/13/2017
#Purpose: Mulitiplies the 2 dominoes
#Inputs: Self, Domino
#Outputs: Result
#====================================================
    def __mul__(self, domino):
        a = self.value // 10
        b = self.value % 10
        if a > b:
            domino1 = b * 10 + a
        else:
            domino1 = self.value

        x = domino.value // 10
        y = domino.value % 10
        if x > y:
            domino2 = y * 10 + x
        else:
            domino2 = domino.value

        ans = domino1 * domino2

        answer = Domino(ans, self.size, self.diameter, self.gap)

        return answer
#====================================================
#Author: Eric Zhou
#Date: 12/13/2017
#Purpose: Determines if domino1 > domino2
#Inputs: Self, Domino
#Outputs: Boolean
#====================================================
    def __gt__(self, domino):
        a = self.value // 10
        b = self.value % 10
        if a > b:
            domino1 = b * 10 + a
        else:
            domino1 = self.value
            
        c = domino.value // 10
        d = domino.value % 10
        if c > d:
            domino2 = d * 10 + c
        else:
            domino2 = domino.value

        if not domino1 > domino2:
            greaterThan = False
        else:
            greaterThan = True

        return greaterThan
#====================================================
#Author: Eric Zhou
#Date: 12/13/2017
#Purpose: Determines if domino1 < domino2
#Inputs: Self, Domino
#Outputs: Boolean
#====================================================
    def __lt__(self, domino):
        a = self.value // 10
        b = self.value % 10
        if a > b:
            domino1 = b * 10 + a
        else:
            domino1 = self.value
            
        c = domino.value // 10
        d = domino.value % 10
        if c > d:
            domino2 = d * 10 + c
        else:
            domino2 = domino.value

        if domino1 < domino2:
            lessThan = True
        else:
            lessThan = False

        return lessThan
#====================================================
#Author: Eric Zhou
#Date: 12/13/2017
#Purpose: Determines if domino1 >= domino2
#Inputs: Self, Domino
#Outputs: Boolean
#====================================================
    def __gtet__(self, domino):
        a = self.value // 10
        b = self.value % 10
        if a > b:
            domino1 = b * 10 + a
        else:
            domino1 = self.value
            
        c = domino.value // 10
        d = domino.value % 10
        if c > d:
            domino2 = d * 10 + c
        else:
            domino2 = domino.value

        if domino1 >= domino2:
            greaterThan = True
        else:
            greaterThan = False

        return greaterThan
    
#====================================================
#Author: Eric Zhou
#Date: 12/13/2017
#Purpose: Determines if domino1 <= domino2
#Inputs: Self, Domino
#Outputs: Boolean
#====================================================
    
    def __ltet__(self, domino):
        
        a = self.value // 10
        b = self.value % 10
        if a > b:
            domino1 = b * 10 + a
        else:
            domino1 = self.value
            
        c = domino.value // 10
        d = domino.value % 10
        if c > d:
            domino2 = d * 10 + c
        else:
            domino2 = domino.value

        if domino1 <= domino2:
            lessThan = True
        else:
            lessThan = False

        return lessThan
    
#====================================================
#Author: Eric Zhou
#Date: 12/13/2017
#Purpose: Determines if domino1 == domino2
#Inputs: Self, Domino
#Outputs: Boolean
#====================================================
    
    def __eq__(self, domino):
        a = self.value // 10
        b = self.value % 10
        if a > b:
            domino1 = b * 10 + a
        else:
            domino1 = self.value
            
        c = domino.value // 10
        d = domino.value % 10
        if c > d:
            domino2 = d * 10 + c
        else:
            domino2 = domino.value

        if domino1 == domino2:
            equal = True
        else:
            equal = False

        return equal
    
#====================================================
#Author: Eric Zhou
#Date: 12/13/2017
#Purpose: Determines if domino1 != domino2
#Inputs: Self, Domino
#Outputs: Boolean
#====================================================
    
    def __ne__(self, domino):
        a = self.value // 10
        b = self.value % 10
        if a > b:
            domino1 = b * 10 + a
        else:
            domino1 = self.value
            
        c = domino.value // 10
        d = domino.value % 10
        if c > d:
            domino2 = d * 10 + c
        else:
            domino2 = domino.value

        if not domino1 == domino2:
            notEqual = True
        else:
            notEqual = False

        return notEqual
    

#SUBPROGRAMS               
# of Dots, vertical/horizontal, face up or face down
#====================================================
#Author: Eric Zhou
#Date: 11/15/2017
#Purpose: Gets custom value for dominoes and display it
#Inputs: Nine
#Outputs: None
#====================================================
def mainProgram():
    myDomino = Domino()
    secondDomino = Domino()
        
    myDomino.value = int(valEntry.get())
    secondDomino.value = int(valEntry2.get())
    
    sValue.set(value=myDomino.value)    
    sValue2.set(value=secondDomino.value)
    
    checkValue = myDomino.getValue()
    checkValue2 = secondDomino.getValue(1)
    if checkValue == True and checkValue2 == True:
        t.delete(1.0, END)
        c.focus_set()   
        secondDomino.setGUISize()
        myDomino.setGUISize()
        myDomino.setOrientation()
        myDomino.setFace()   
        myDomino.draw(c, secondDomino)
        texts()
    
#====================================================
#Author: Eric Zhou
#Date: 11/16/2017
#Purpose: Gets random value of dominoes and display it
#Inputs: None
#Outputs: None
#====================================================
def goRandomize():
    t.delete(1.0, END)
    myDomino = Domino()
    secondDomino = Domino()
    newVal = myDomino.randomize()
    newVal2 = secondDomino.randomize()
    while newVal + newVal2 > 99:
        newVal = myDomino.randomize()
        newVal2 = secondDomino.randomize()
    c.focus_set()
    myDomino.setGUISize()
    secondDomino.setGUISize()
    myDomino.setOrientation()
    myDomino.setFace()
    myDomino.draw(c, secondDomino)
    texts()

def texts():
    t.insert(END, "Value: " + str(sValue.get()) + " ")
    t.insert(END, "\n" + "Value #2: " + str(sValue2.get()) + " " )
    t.insert(END, "\n" + "Result: " + str(resultDomino.get()) + "  ")
    t.insert(END, "\n" + "Size: " + str(sizeScale.get()))
    
#====================================================
#Author: Eric Zhou
#Date: 11/17/2017
#Purpose: Changes the size of the dominoes
#Inputs: None
#Outputs: None
#====================================================
def changeSize():
    t.delete(1.0, END)
    myDomino = Domino()
    secondDomino = Domino()
    checkValue = myDomino.getValue()
    if checkValue == True:
        myDomino.value = int(sValue.get())
        secondDomino.value = int(sValue2.get())
        myDomino.setGUISize()
        secondDomino.setGUISize()
        myDomino.setOrientation()
        myDomino.setFace()
        myDomino.draw(c, secondDomino)
        texts()

#====================================================
#Author: Eric Zhou
#Date: 11/20/2017
#Purpose: Changes the color of the dominoes
#Inputs: None
#Outputs: None
#====================================================
def changeColor():
    ogColor = int(originalColor.get())
    getColor = random.randint(0,6)
    while ogColor == getColor:
        getColor = random.randint(0,6)
        
    if getColor == 0:
        color.set(value="black")
    if getColor == 1:
        color.set(value="red")
    if getColor == 2:
        color.set(value="orange")
    if getColor == 3:
        color.set(value="yellow")
    if getColor == 4:
        color.set(value="green")
    if getColor == 5:
        color.set(value="blue")
    if getColor == 6:
        color.set(value="purple")

    originalColor.set(value=getColor)
        
#============================================================
#Author: Eric Zhou
#Date: 11/17/2017
#Purpose: When a certain key is pressed, calls certain methods
#Inputs: Event (key pressed)
#Outputs: None
#===============================================================
def keyPressed(event):
    myDomino = Domino()
    secondDomino = Domino()
    valid = True
    if event.char == "x":
        mainWindow.destroy()
        valid = False

    elif event.char == "c":
        clear()
        
    elif event.char == "f":
        if int(sizeScale.get()) < 100:
            newSize = int(sizeScale.get()) + 1
            sizeScale.set(value=newSize)
        else:
            sizeScale.set(value="100")

        changeSize()
            
    elif event.char == "g":
        if int(sizeScale.get()) >31:
            newSize = int(sizeScale.get()) - 1
            sizeScale.set(value=newSize)
        else:
            sizeScale.set(value="30")
            
        changeSize()

    elif event.char == "v":
        changeColor()
        myDomino.setGUISize()
        secondDomino.setGUISize()
        myDomino.value = int(sValue.get())
        secondDomino.value = int(sValue2.get())
        myDomino.draw(c, secondDomino)

    elif event.char == "d":
        t.delete(1.0, END)
        newVal = myDomino.randomize()
        newVal2 = secondDomino.randomize()
        while newVal + newVal2 > 99:
            newVal = myDomino.randomize()
            newVal2 = secondDomino.randomize()
            
        sValue.set(value=newVal)    
        sValue2.set(value=newVal2)
        secondDomino.setGUISize()
        myDomino.setGUISize()
        myDomino.setOrientation()
        myDomino.setFace()
        myDomino.draw(c, secondDomino)
        texts()
        
        valid = False


#====================================================
#Author: Eric Zhou
#Date: 11/15/2017
#Purpose: Clears canvas
#Inputs: None
#Outputs: None
#====================================================
        
def clear():
    c.delete("all")
    c.focus_set()
    

global c

#Tkinter Stuff
mainWindow = Tk()
mainWindow.title("Dominoes")

#Menu
menubar = Menu(mainWindow)

#File Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open",
                     command=lambda:messagebox.showerror("Error", "No saved files found!"))
filemenu.add_command(label="Save",
                     command=lambda:messagebox.showerror("Error", "This feature is not added in yet!"))
filemenu.add_separator()
filemenu.add_command(label="Exit",
                     command=lambda:(messagebox.showinfo("Bye!", "Good Bye, User!"),mainWindow.destroy()))
menubar.add_cascade(label="File", menu=filemenu)

#Edit Menu
editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label="Undo",
                     command=lambda:messagebox.showerror("Error", "This feature is not added yet!"))
editmenu.add_command(label="Redo",
                     command=lambda:messagebox.showerror("Error", "This feature is not added yet!"))
menubar.add_cascade(label="Edit", menu=editmenu)

#Help Menu
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="About",
                     command=lambda:messagebox.showinfo(" About ", " This program was created by Eric Zhou :) "))
helpmenu.add_command(label="Restart",
                     command=lambda:restart())
menubar.add_cascade(label="Help", menu=helpmenu)

#Main Window Config
mainWindow.config(menu=menubar, bg="steelblue", width= 1080, height = 500)

#String Vars
#s is for storing purposes, eg storing value = sValue
sValue = StringVar()
sValue.set(value="0")
sOrientation = StringVar()
sOrientation.set(value=True)
sFace = StringVar()
sFace.set(value=False)
length = StringVar()
length.set(value="")
countX = StringVar()
countX.set(value="0")
countY = StringVar()
countY.set(value="0")
valRandom = StringVar()
sizeCount = StringVar()
sizeCount.set(value="0")
color = StringVar()
color.set(value="black")
originalColor = StringVar()
originalColor.set(value="0")
operator = IntVar()
operator.set(value="1")
sValue2 = StringVar()
sValue2.set(value="0")
resultDomino = StringVar()
getX = StringVar()
getX.set(value="0")
getY = StringVar()
getY.set(value="0")

#Display Dominos Canvas
c = Canvas(mainWindow, highlightthickness = 4, highlightbackground="black", bg="white", width=783, height=425)
c.place(x=242, y=25)
c.bind("<Key>", keyPressed)
c.focus_set()

#=======================================================
#Input Box
Frame(mainWindow, highlightthickness = 4, highlightbackground="black", bg= "white", height = 220, width =175).place(x=25, y=55)
Label(mainWindow, bg="steelblue", fg="white", font=("Times, bold", 18), text="Dominos").place(x=65, y=15)
Label(mainWindow, bg="white", fg="black", font=("Times", 12), text="Enter value: ").place(x=30, y=60)
valEntry = Entry(mainWindow, textvariable=sValue, width=10, relief = "solid")
valEntry.place(x=125, y=63)
Label(mainWindow, bg="white", fg="black", font=("Times", 12), text="Enter value#2: ").place(x=30, y=90)
valEntry2 = Entry(mainWindow, textvariable=sValue2, width=10, relief = "solid")
valEntry2.place(x=125, y=93)


#Size scale
Label(mainWindow, bg="white", fg="black", text="Size: ", font=("Times", 14)).place(x=30, y=120)
sizeScale = Scale(mainWindow, from_=30, to=100, bg="black", fg="white", orient=HORIZONTAL, command=lambda x: changeSize())
sizeScale.place(x=80, y=120)

#Buttons
Button(mainWindow, text="Proceed", font=("Times bold", 12), bg="steelblue", fg="white", relief = "solid", command=lambda:(mainProgram())).place(x=78, y=169)
Radiobutton(mainWindow, text="Add (+)", fg="black", font=("Arial",10), bg="white", value = 1, variable=operator).place(x=30,y=215)
Radiobutton(mainWindow, text="Sub (-)", fg="black", font=("Arial",10), bg="white", value = 2, variable=operator).place(x=120,y=215)
Radiobutton(mainWindow, text="Mul (*)", fg="black", font=("Arial",10), bg="white", value = 3, variable=operator).place(x=30,y=235)

#Text 
t = Text(mainWindow,height=4, highlightthickness=3, highlightbackground="black", width=21,bg="white",fg="black", relief = "solid")
t.place(x=25, y= 287)
t.tag_remove(SEL,"1.0", END)

#Below Text Labels
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 10), text="Press 'd' to draw a random domino!").place(x=5, y= 365)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 10), text="Press 'f' to increase domino's size!").place(x=5, y= 385)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 10), text="Press 'g' to decrease domino's size!").place(x=5, y= 405)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 10), text="Press 'c' to clear the canvas!").place(x=5, y= 425)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 10), text="Press 'v' to change domino's color!").place(x=5, y= 445)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 10), text="Press 'x' to exit the program!").place(x=5, y= 465)

Label(mainWindow, fg="white", bg="steelblue", font=("Times bold", 12), text="Domino:").place(x=242, y= 465)
Label(mainWindow, fg="white", bg="steelblue", font=("Times bold", 12), text="x = ").place(x=312, y= 465)
x = Entry(mainWindow, textvariable=getX, width=2, relief = "solid")
x.place(x=343, y=468)
Label(mainWindow, fg="white", bg="steelblue", font=("Times bold", 12), text="y = ").place(x=372, y= 465)
y = Entry(mainWindow, textvariable=getY, width=2, relief = "solid")
y.place(x=403, y=468)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Range: 0 - 99").place(x=425, y= 465)
#========================================================


mainloop()


