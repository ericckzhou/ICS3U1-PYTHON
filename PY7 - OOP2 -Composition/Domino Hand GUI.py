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
#====================================================

class Domino():
    def __init__(self, value = 0, size=30, diameter = 0, gap = 0, orientation = True, face = False):
        #value of domino
        self.value = value
        if not self.value in range(0,100):
            self.value = 0
        #size of domino
        self.size = size
        if not self.size in range(30,101):
            self.size = 30
        #diameter of the domino
        self.diameter = size / 5
        #gap of domino
        self.gap = diameter / 2
        #orientation of domino
        self.orientation = orientation
        if not (self.orientation == True or self.orientation == False):
            self.orientation = True
        #face of domino
        self.face = face
        if not (self.face == True or self.face == False):
            self.face = True
            
    
#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Return value of dominoes as a string
#Inputs: Self
#Outputs: None
#====================================================
        
    def __str__(self):
        self.value = str(sValue.get())
        
#====================================================
#Author: Eric Zhou
#Date: 11/13/2017
#Purpose: Getting a valid value from user
#Inputs: Self
#Outputs: Return Valid value / error messages
#====================================================
    def getValue(self):
        valid = True
        if not (str(self.value).isdigit()):
            valid = False
            messagebox.showerror("Error", "Your last value input was not a positive valid integer! ")

        if valid == True:  
            if not int(self.value) in range(0,100):
                valid = False
                messagebox.showerror("Error", "Your last value input was not in range 0-99! ")  
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
    def setSize(self):
        self.size = int(sizeScale.get())
        self.diameter = self.size / 5
        self.gap = self.diameter / 2
        
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
    def draw(self, canvas, x=0, y=0):
        x = str(getX.get())
        y = str(getY.get())
                
        if (not x.isdigit() or not y.isdigit()):
            getX.set(value=0)
            getY.set(value=0)
            x=0
            y=0

        x = int(x)
        y = int(y)
        if x > 50 or y > 50 or x <0 or y <0:
            getX.set(value=0)
            getY.set(value=0)
            x=0
            y=0
            
        canvas.delete("all")
        canvasetColor = str(color.get())
        canvas.create_rectangle(self.size+x, self.size*2+y, self.size *2, self.size*3+x, width=4+y, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size+x,self.size+y, self.size *2, self.size *2+x, width=4+y, fill=getColor, outline="gray")

        canvas.create_rectangle(self.size*2+x, self.size *2+y, self.size *3+x, self.size *3+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*3+x, self.size *2+y, self.size *4+x, self.size *3+y, width=4, fill=getColor, outline="gray")
        
        canvas.create_rectangle(self.size*4+x, self.size *2+y, self.size *5+x, self.size *3+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*4+x, self.size *2+y, self.size *5+x, self.size+y, width=4, fill=getColor, outline="gray")
        
        dot1 = 0 #Top
        dot2 = 0 #Bottom
        
        if self.value <=9:
            dot1 = 0
            dot2 = self.value

        if self.value > 10:
            dot1 = self.value // 10
            dot2 = self.value % 10

        self.drawDots(dot1, 0, 0, 0, 0)
        self.drawDots(dot2, 0, 1, 0, 1)

        self.face = True
        self.orientation = False
        dot1, dot2 = dot2, dot1
        self.drawDots(dot1, 1, 1, 1, 1)
        self.drawDots(dot2, 2, 1, 2, 1)

        self.face = False
        self.orientation = True
        dot1, dot2 = dot2, dot1
        self.drawDots(dot1, 3, 1, 3, 1)
        self.drawDots(dot2, 3, 0, 3, 0)

        self.face = False
        self.orientation = False
        canvas.create_rectangle(self.size*5, self.size, self.size *6, self.size *2, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*6, self.size, self.size *7, self.size *2, width=4, fill=getColor, outline="gray")

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
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")

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
#Date: 11/23/2017
#Purpose: Creating Hand Class
#Inputs: value, size
#Outputs: None
#====================================================
class Hand():
#====================================================
#Author: Eric Zhou
#Date: 11/23/2017
#Purpose: Constructing class
#Inputs: firstDomino, secondDomino, thirdDomino
#Outputs: None
#Methods: ===========================================
#__init__:       - Constructs the Hand class.
#__str__:        - Returns the string version of domino hand
#setSize:        - Sets the Size of domino
#sort:           - Rearranges the hand from least to greatest
#roll:           - Rolls random value for domno hand.
#draw:           - Draws the domino hand.
#getRun:         - Gets the run of the domino hand.
#====================================================
    def __init__(self, firstDomino=Domino(), secondDomino=Domino(), thirdDomino=Domino()):
        self.firstDomino = firstDomino
        self.secondDomino = secondDomino
        self.thirdDomino = thirdDomino
        
#====================================================
#Author: Eric Zhou
#Date: 11/23/2017
#Purpose: Returning the string version of the valued dominoes
#Inputs: Self
#Outputs: value of each dominoes
#====================================================
    def __str__(self):
        return str(self.firstDomino.value + ' - ' + self.secondDomino.value + ' - ' + self.thirdDomino.value)
    
#====================================================
#Author: Eric Zhou
#Date: 11/23/2017
#Purpose: set the size of the dominos
#Inputs: Self
#Outputs: None
#====================================================
    def setSize(self):
        size = int(sizeScale.get())
        self.firstDomino.setSize()
        self.secondDomino.setSize()
        self.thirdDomino.setSize()

#====================================================
#Author: Eric Zhou
#Date: 11/23/2017
#Purpose: sorts the dominoes from least to greatest
#Inputs: Self
#Outputs: None
#====================================================
    def sort(self):
        a = self.firstDomino.value
        b = self.secondDomino.value
        c = self.thirdDomino.value
        ogDomino1.set(value=a)
        ogDomino2.set(value=b)
        ogDomino3.set(value=c)
        
        if a > b:
            a, b = b, a
        if a > c:
            a, c = c, a
        if c < a:
            c, a = a, c
        if c < b:
            c, b = b, c

        self.firstDomino.value = a
        self.secondDomino.value = b
        self.thirdDomino.value = c
        
#====================================================
#Author: Eric Zhou
#Date: 11/23/2017
#Purpose: roll for a random domino value for each one
#Inputs: Self
#Outputs: None
#====================================================
    def roll(self):
        self.firstDomino.value = random.randint(0, 99)
        self.secondDomino.value = random.randint(0, 99)
        self.thirdDomino.value = random.randint(0, 99)
        
        ogDomino1.set(value=self.firstDomino.value)
        ogDomino2.set(value=self.secondDomino.value)
        ogDomino3.set(value=self.thirdDomino.value)
    
#====================================================
#Author: Eric Zhou
#Date: 11/24/2017
#Purpose: Draws new rectangle with different x's and y's value
#Inputs: Self
#Outputs: None
#====================================================
    def draw(self, canvas, x=0, y=0):
        x = str(getX.get())
        y = str(getY.get())
                
        if (not x.isdigit() or not y.isdigit()):
            getX.set(value=0)
            getY.set(value=0)
            x=0
            y=0

        x = int(x)
        y = int(y)
        if x > 50 or y > 50 or x <0 or y <0:
            getX.set(value=0)
            getY.set(value=0)
            x=0
            y=0
            
        getColor = str(color.get())
        self.size = int(sizeScale.get())

        canvas.delete("all")

        #Draws rectangle for dominoes
        canvas.create_rectangle(self.size*1+x, self.size *2+y, self.size *2+x, self.size *3+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*2+x, self.size *2+y, self.size *3+x, self.size *3+y, width=4, fill=getColor, outline="gray")   
        canvas.create_rectangle(self.size*4+x, self.size *2+y, self.size *5+x, self.size *3+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*5+x, self.size *2+y, self.size *6+x, self.size *3+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*7+x, self.size *2+y, self.size *8+x, self.size *3+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*8+x, self.size *2+y, self.size *9+x, self.size *3+y, width=4, fill=getColor, outline="gray")
        
        canvas.create_rectangle(self.size*1+x, self.size *4+y, self.size *2+x, self.size *5+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*2+x, self.size *4+y, self.size *3+x, self.size *5+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*4+x, self.size *4+y, self.size *5+x, self.size *5+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*5+x, self.size *4+y, self.size *6+x, self.size *5+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*7+x, self.size *4+y, self.size *8+x, self.size *5+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*8+x, self.size *4+y, self.size *9+x, self.size *5+y, width=4, fill=getColor, outline="gray")

        canvas.create_rectangle(self.size*1+x, self.size *6+y, self.size *2+x, self.size *7+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*2+x, self.size *6+y, self.size *3+x, self.size *7+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*4+x, self.size *6+y, self.size *5+x, self.size *7+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*5+x, self.size *6+y, self.size *6+x, self.size *7+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*7+x, self.size *6+y, self.size *8+x, self.size *7+y, width=4, fill=getColor, outline="gray")
        canvas.create_rectangle(self.size*8+x, self.size *6+y, self.size *9+x, self.size *7+y, width=4, fill=getColor, outline="gray")

        #Draws dots for original
        dot1 = int(ogDomino1.get()) // 10
        dot2 = int(ogDomino1.get()) % 10

        dot3 = int(ogDomino2.get()) // 10
        dot4 = int(ogDomino2.get()) % 10

        dot5 = int(ogDomino3.get()) // 10
        dot6 = int(ogDomino3.get()) % 10

        self.firstDomino.face = True
        self.firstDomino.orientation = False

        self.secondDomino.face = True
        self.secondDomino.orientation = False

        self.thirdDomino.face = True
        self.thirdDomino.orientation = False

        self.firstDomino.drawDots(c, dot1, 0, 1, 0, 1)
        self.firstDomino.drawDots(c, dot2, 1, 1, 1, 1)

        self.secondDomino.drawDots(c, dot3, 3, 1, 3, 1)
        self.secondDomino.drawDots(c, dot4, 4, 1, 4, 1)

        self.thirdDomino.drawDots(c, dot5, 6, 1, 6, 1)
        self.thirdDomino.drawDots(c, dot6, 7, 1, 7, 1)

        self.sort()

        #Draw dots for sorted domino
        dot1 = self.firstDomino.value // 10
        dot2 = self.firstDomino.value % 10

        dot3 = self.secondDomino.value // 10
        dot4 = self.secondDomino.value % 10

        dot5 = self.thirdDomino.value // 10
        dot6 = self.thirdDomino.value % 10
        
        self.firstDomino.drawDots(c, dot1, 0, 3, 0, 3)
        self.firstDomino.drawDots(c, dot2, 1, 3, 1, 3)

        self.secondDomino.drawDots(c, dot3, 3, 3, 3, 3)
        self.secondDomino.drawDots(c, dot4, 4, 3, 4, 3)

        self.thirdDomino.drawDots(c, dot5, 6, 3, 6, 3)
        self.thirdDomino.drawDots(c, dot6, 7, 3, 7, 3)
        
        runDom1 = int(runDomino1.get())
        runDom2 = int(runDomino2.get())
        runDom3 = int(runDomino3.get())

        #Draw dots after rearranging
        dot7 = runDom1 // 10
        dot8 = runDom1 % 10

        dot9 = runDom2 // 10
        dot10 = runDom2 % 10

        dot11 = runDom3 // 10
        dot12 = runDom3 % 10
        
        self.firstDomino.drawDots(c, dot7, 0, 5, 0, 5)
        self.firstDomino.drawDots(c, dot8, 1, 5, 1, 5)

        self.secondDomino.drawDots(c, dot9, 3, 5, 3, 5)
        self.secondDomino.drawDots(c, dot10, 4, 5, 4, 5)

        self.thirdDomino.drawDots(c, dot11, 6, 5, 6, 5)
        self.thirdDomino.drawDots(c, dot12, 7, 5, 7, 5)
        
#====================================================
#Author: Eric Zhou
#Date: 11/25/2017
#Purpose: Gets the run of the dominoes hand
#Inputs: Self
#Outputs: None
#====================================================
    def getRun(self):
        run = 0
        a = int(self.firstDomino.value)
        b = int(self.secondDomino.value)
        c = int(self.thirdDomino.value)
        
        a1 = a // 10
        a2 = a % 10

        b1 = b // 10
        b2 = b % 10

        c1 = c // 10
        c2 = c % 10
        
        if b2 != c1:
            if b1 == c1 and not a2 == b1:
                b1, b2 = b2, b1
                
            elif b1 == c2 and not a2 == b1:
                b1, b2, c1, c2 = b2, b1, c2, c1
                
            elif b2 == c2:
                c1, c2 = c2, c1
                
        if a2 != b1:
            if a1 == b1:
                a1, a2 = a2, a1
                
            elif a1 == b2 and not b2 == c1:
                a1, a2, b1, b2 = a2, a1, b2, b1
                
            elif a2 == b2 and not b2 == c1:
                b1, b2 = b2, b1

        if not (b2 == c1 and a2 == b1):
    
            if a1 == b2 and b1 == c1:
                a1, a2, b1, b2, c1, c2 = a2, a1, b2, b1, c1, c2
                
            elif a1 == b2 and b1 == c2:
                a1, a2, b1, b2, c1, c2 = a2, a1, b2, b1, c2, c1
                
            elif a2 == b2 and b1 == c1:
                b1, b2, c1, c2 = b2, b1, c1, c2
                
            elif a2 == b2 and b1 == c2:
                b1, b2, c1, c2 = b2, b1, c2, c1
                
            elif a1 == c1 and not (a2 == b1 or b2 == c1):
                a1, a2, b1, b2, c1, c2 = b1, b2, c1, c2, a1, a2
                
            elif a1 == c1 and b2 != c1:
                a1, a2, b1, b2, c1, c2 = c2, c1, a1, a2, b1, b2
                
            elif a2 == c1 and not (a2 == b1 or b2 == c1):
                b1, b2, c1, c2 = c1, c2, b1, b2

            elif a1 == c2 and a2 != b1:
                a1, a2, b1, b2, c1, c2 = b1, b2, c1, c2, a1, a2
                
            elif a1 == c2 and b2 != c1:
                a1, a2, b1, b2, c1, c2 = c1, c2, a1, a2, b1, b2

            elif a2 == c2 and a2 != b1:
                a1, a2, b1, b2, c1, c2 = b1, b2, c1, c2, a2, a1
                
            elif a2 == c2 and b2 != c1:
                b1, b2, c1, c2 = c2, c1, b1, b2

        if (a2 == b1 and b2 != c1) or (b2 == c1 and a2 != b1):
            run = 2

        elif a2 == b1 and b2 == c1:
            run = 3

        if run == 0:
            newRun = int(runNumber0.get()) + 1
            runNumber0.set(value=newRun)
        elif run == 2:
            newRun = int(runNumber2.get()) + 1
            runNumber2.set(value=newRun)
        elif run == 3:
            newRun = int(runNumber3.get()) + 1
            runNumber3.set(value=newRun)
            
        runNumber.set(value=run)
        
        value1 = (a1 * 10) + a2
        value2 = (b1 * 10) + b2
        value3 = (c1 * 10) + c2
        
        runDomino1.set(value=value1)
        runDomino2.set(value=value2)
        runDomino3.set(value=value3)

        return run
        
#SUBPROGRAMS
#====================================================
#Author: Eric Zhou
#Date: 11/25/2017
#Purpose: Gets entered value
#Inputs: Self
#Outputs None
#====================================================
def mainProgram():
    myHand = Hand()
    t.delete(1.0, END)
    c.focus_set()
    myHand.firstDomino.value = valEntry1.get()
    myHand.secondDomino.value = valEntry2.get()
    myHand.thirdDomino.value = valEntry3.get()
    valid1 = myHand.firstDomino.getValue()
    valid2 = myHand.secondDomino.getValue()
    valid3 = myHand.thirdDomino.getValue()
    
    if valid1 == True and valid2 == True and valid3 == True:
        myHand.firstDomino.value = int(valEntry1.get())
        myHand.secondDomino.value = int(valEntry2.get())
        myHand.thirdDomino.value = int(valEntry3.get())
        myHand.setSize()
        myHand.sort()
        myHand.getRun()
        myHand.draw(c)
        insertText()

#====================================================
#Author: Eric Zhou
#Date: 11/25/2017
#Purpose: Inserts the text to the text box
#Inputs: Self
#Outputs: None
#====================================================
def insertText():
    myHand = Hand()
    t.insert(END, "------Original------")
    t.insert(END, "\n" + "Domino #1: " + str(ogDomino1.get()) + " ")
    t.insert(END, "\n" + "Domino #2: " + str(ogDomino2.get()))
    t.insert(END, "\n" + "Domino #3: " + str(ogDomino3.get()))
    
    t.insert(END, "\n" + "-------Sorted-------")
    t.insert(END, "\n" + "Domino #1: " + str(myHand.firstDomino.value) + " ")
    t.insert(END, "\n" + "Domino #2: " + str(myHand.secondDomino.value))
    t.insert(END, "\n" + "Domino #3: " + str(myHand.thirdDomino.value))
    t.insert(END, "\n" + "---------------------")
    
    t.insert(END, "\n" + "Size: " + str(sizeScale.get()))
    t.insert(END, "\n" + "Run: " + str(runNumber.get()))
    
    t.insert(END, "\n" + "------Rearranged-----")
    t.insert(END, "\n" + "Domino #1: " + str(runDomino1.get()) + " ")
    t.insert(END, "\n" + "Domino #2: " + str(runDomino2.get()))
    t.insert(END, "\n" + "Domino #3: " + str(runDomino3.get()))    
    
#====================================================
#Author: Eric Zhou
#Date: 11/17/2017
#Purpose: Changes the size of the dominoes
#Inputs: None
#Outputs: None
#====================================================

def changeSize():
    t.delete(1.0, END)
    myHand = Hand()
    myHand.setSize()
    myHand.firstDomino.value = int(valEntry1.get())
    myHand.secondDomino.value = int(valEntry2.get())
    myHand.thirdDomino.value = int(valEntry3.get())
    myHand.getRun()
    myHand.draw(c)
    insertText()


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
    myHand = Hand()

    if event.char == "x":
        mainWindow.destroy()


    elif event.char == "c":
        clear()
        
    elif event.char == "d":
        if int(sizeScale.get()) < 100:
            newSize = int(sizeScale.get()) + 1
            sizeScale.set(value=newSize)
        else:
            sizeScale.set(value="100")
        changeSize()

            
    elif event.char == "f":
        if int(sizeScale.get()) >31:
            newSize = int(sizeScale.get()) - 1
            sizeScale.set(value=newSize)
        else:
            sizeScale.set(value="30")
        changeSize()
            

    elif event.char == "v":
        changeColor()
        myHand.draw(c)
        
    elif event.char == "h":
        t.delete(1.0, END)
        myHand.roll()
        myHand.getRun()
        myHand.draw(c)
        insertText()


    elif event.char == "g":
        for i in range(0,9999):
            myHand.roll()
            myHand.getRun()
            
        t.delete(1.0, END)
        myHand.roll()
        myHand.draw(canvas = c)
        insertText()
        myHand.getRun()
        a1 = int(runNumber0.get())
        b1 = int(runNumber2.get())
        c1 = int(runNumber3.get())
        percent0 = round(((a1 / 10000) * 100), 2)
        percent2 = round(((b1 / 10000) * 100), 2)
        percent3 = round(((c1 / 10000) * 100), 2)
        t.insert(END, "\n" + "---------------------")
        t.insert(END, "\n" + "Run = 0: " + str(percent0)+ "%")
        t.insert(END, "\n" + "Run = 2: " + str(percent2)+ "%")
        t.insert(END, "\n" + "Run = 3: " + str(percent3)+ "%")

        runNumber0.set(value=0)
        runNumber2.set(value=0)
        runNumber3.set(value=0)
          
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
    
#====================================================
#Author: Eric Zhou
#Date: 11/27/2017
#Purpose: Generates a new hand for user
#Inputs: Self
#Outputs: None
#====================================================
def newHand():
    myHand = Hand()
    t.delete(1.0, END)
    myHand.roll()
    myHand.getRun()
    myHand.draw(c)
    insertText()

global c

#Tkinter Stuff
mainWindow = Tk()
mainWindow.title("Dominoes")

#Menu
menubar = Menu(mainWindow)

#File Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Hand",
                     command=lambda:(newHand()))
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
mainWindow.config(menu=menubar, bg="steelblue", width= 1280, height = 871)

#String Vars
#s is for storing purposes, eg storing value = sValue
sValue = StringVar()
sValue.set(value="0")
sOrientation = StringVar()
sOrientation.set(value=True)
sFace = StringVar()
sFace.set(value=False)
sizeCount = StringVar()
sizeCount.set(value="0")
color = StringVar()
color.set(value="black")
originalColor = StringVar()
originalColor.set(value="0")
runNumber = StringVar()
runNumber.set(value="0")
runNumber0 = StringVar()
runNumber0.set(value="0")
runNumber2 = StringVar()
runNumber2.set(value="0")
runNumber3 = StringVar()
runNumber3.set(value="0")

#ORIGINAL (Before sorted)
ogDomino1 = StringVar()
ogDomino1.set(value="0")
ogDomino2 = StringVar()
ogDomino2.set(value="0")
ogDomino3 = StringVar()
ogDomino3.set(value="0")

runDomino1 = StringVar()
runDomino1.set(value="0")
runDomino2 = StringVar()
runDomino2.set(value="0")
runDomino3 = StringVar()
runDomino3.set(value="0")

getX = StringVar()
getX.set(value="0")
getY = StringVar()
getY.set(value="0")
#Display Dominos Canvas
c = Canvas(mainWindow, highlightthickness = 4, highlightbackground="black", bg="white", width=983, height=825)
c.place(x=242, y=25)
c.bind("<Key>", keyPressed)
c.focus_set()

#=======================================================
#Input Box
Frame(mainWindow, highlightthickness = 4, highlightbackground="black", bg= "white", height = 210, width =175).place(x=25, y=55)
Label(mainWindow, bg="steelblue", fg="white", font=("Times, bold", 18), text="Dominos").place(x=65, y=15)
Label(mainWindow, bg="white", fg="black", font=("Times", 14), text="Domino #1:").place(x=30, y=60)
Label(mainWindow, bg="white", fg="black", font=("Times", 14), text="Domino #2:").place(x=30, y=80)
Label(mainWindow, bg="white", fg="black", font=("Times", 14), text="Domino #3:").place(x=30, y=100)
valEntry1 = Entry(mainWindow, textvariable=ogDomino1, width=10, relief = "solid")
valEntry1.place(x=125, y=63)
valEntry2 = Entry(mainWindow, textvariable=ogDomino2, width=10, relief = "solid")
valEntry2.place(x=125, y=83)
valEntry3 = Entry(mainWindow, textvariable=ogDomino3, width=10, relief = "solid")
valEntry3.place(x=125, y=103)

#Size scale
Label(mainWindow, bg="white", fg="black", text="Size: ", font=("Times", 14)).place(x=30, y=120)
sizeScale = Scale(mainWindow, from_=30, to=100, bg="black", fg="white", orient=HORIZONTAL, command=lambda x: changeSize())
sizeScale.place(x=80, y=125)
sizeScale.set(value=50)

#Buttons
Button(mainWindow, text="Proceed", font=("Times bold", 12), bg="steelblue", fg="white", relief = "solid", command=lambda:(mainProgram())).place(x=78, y=174)
Button(mainWindow, text="Clear", font=("Times bold", 12), bg="steelblue", fg="white", relief = "solid", width=6, command=lambda:(clear())).place(x=80, y=215)

#Text 
t = Text(mainWindow,height=20, highlightthickness=3, highlightbackground="black", width=21,bg="white",fg="black", relief = "solid")
t.place(x=25, y= 285)
        
t.tag_remove(SEL,"1.0", END)

#Below Text Labels
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press each letter with CAPS OFF!").place(x=5, y= 645)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'D' to increase domino's size!").place(x=5, y= 665)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'F' to decrease domino's size!").place(x=5, y= 685)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'C' to clear the canvas!").place(x=5, y= 705)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'V' to change domino's color!").place(x=5, y= 725)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'H' to get random hand!").place(x=5, y= 745)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'G' to generate 10000 hands!").place(x=5, y= 765)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'X' to exit the program!").place(x=5, y= 785)

Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Range: 0-50 ").place(x=60, y= 820)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="X = ").place(x=5, y= 810)
x = Entry(mainWindow, textvariable=getX, width=2, relief = "solid")
x.place(x=35, y=813)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Y = ").place(x=5, y= 835)
y = Entry(mainWindow, textvariable=getY, width=2, relief = "solid")
y.place(x=35, y=838)
#=======================================================
    

mainloop()

