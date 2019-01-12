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
#====================================================

class Domino():
    def __init__(self, value = random.randint(0,66), size=30, diameter = 0, gap = 0, orientation = True, face = False):
        self.value = value
        self.size = size
        self.diameter = size / 5
        self.gap = diameter / 2
        self.orientation = orientation
        self.face = face
        
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
    def draw(self):
        c.delete("all")
        getColor = str(color.get())
        c.create_rectangle(self.size, self.size*2, self.size *2, self.size*3, width=4, fill=getColor, outline="gray")
        c.create_rectangle(self.size,self.size, self.size *2, self.size *2, width=4, fill=getColor, outline="gray")
        c.create_rectangle(self.size*2, self.size *2, self.size *3, self.size *3, width=4, fill=getColor, outline="gray")
        c.create_rectangle(self.size*3, self.size *2, self.size *4, self.size *3, width=4, fill=getColor, outline="gray")
        c.create_rectangle(self.size*4, self.size *2, self.size *5, self.size *3, width=4, fill=getColor, outline="gray")
        c.create_rectangle(self.size*4, self.size *2, self.size *5, self.size, width=4, fill=getColor, outline="gray")
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
        c.create_rectangle(self.size*5, self.size, self.size *6, self.size *2, width=4, fill=getColor, outline="gray")
        c.create_rectangle(self.size*6, self.size, self.size *7, self.size *2, width=4, fill=getColor, outline="gray")



#====================================================
#Author: Eric Zhou
#Date: 11/15/2017
#Purpose: Draw the dots of the dominoes
#Inputs: Self
#Outputs: None
#====================================================
        
    def drawDots(self,Dots, x1, y1, x2, y2):
        gap1 = self.gap + self.size
        gap2 = (self.gap * 2) + (self.diameter) +self.size
        gap3 = (self.gap * 3) + (self.diameter * 2) + self.size
        
        dot = 0
        hDot = 0
        
        gapx1 = self.size * x1
        gapx2 = self.size * x2
        gapy1 = self.size * y1
        gapy2 = self.size * y2
        
        valid = False
        
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
                c.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")

            if dot == 2:
                c.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if hDot ==2:
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")

            if dot == 3:
                c.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if hDot == 3:
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")


            if dot == 4 or hDot == 4:
                c.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if dot == 5 or hDot == 5:
                c.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if dot == 6:
                c.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap2 + gapy1, gap1 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap2 + gapy1, gap3 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if hDot == 6:
                c.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap1 + gapy1, gap2 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap3 + gapy1, gap2 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
            if dot == 7:
                c.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap2 + gapy1, gap1 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")   
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap2 + gapy1, gap3 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

            if hDot == 7:
                c.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap1 + gapy1, gap2 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap3 + gapy1, gap2 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                
            if dot == 8 or hDot == 8:
                c.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap2 + gapy1, gap1 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap2 + gapy1, gap3 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap1 + gapy1, gap2 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap3 + gapy1, gap2 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                
            if dot == 9 or hDot == 9:
                #COLUMN 1
                c.create_oval(gap1 + gapx1, gap1 + gapy1, gap1 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap2 + gapy1, gap1 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap1 + gapx1, gap3 + gapy1, gap1 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                #COLUMN 2
                c.create_oval(gap2 + gapx1, gap1 + gapy1, gap2 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap2 + gapy1, gap2 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap2 + gapx1, gap3 + gapy1, gap2 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")
                #COLUMN 3
                c.create_oval(gap3 + gapx1, gap1 + gapy1, gap3 + self.diameter + gapx2, gap1 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap2 + gapy1, gap3 + self.diameter + gapx2, gap2 + self.diameter + gapy2, fill="white")
                c.create_oval(gap3 + gapx1, gap3 + gapy1, gap3 + self.diameter + gapx2, gap3 + self.diameter + gapy2, fill="white")

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
    checkValue = myDomino.getValue()
    if checkValue == True:
        t.delete(1.0, END)
        c.focus_set()
        myDomino.setValue()
        myDomino.setSize()
        myDomino.setOrientation()
        myDomino.setFace()   
        myDomino.draw()
        t.insert(END, "Value: " + str(myDomino.value) + " ")
        t.insert(END, "\n" + "Size: " + str(myDomino.size))
        
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
    newValue = myDomino.randomize()
    sValue.set(value=newValue)
    c.focus_set()
    myDomino.setSize()
    myDomino.setOrientation()
    myDomino.setFace()
    myDomino.draw()
    t.insert(END, "Value: " + str(myDomino.value) + " ")
    t.insert(END, "\n" + "Size: " + str(myDomino.size))
    
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
    checkValue = myDomino.getValue()
    if checkValue == True:
        myDomino.setValue()
        myDomino.setSize()
        myDomino.setOrientation()
        myDomino.setFace()
        myDomino.draw()
        t.insert(END, "Value: " + str(myDomino.value) + " ")
        t.insert(END, "\n" + "Size: " + str(myDomino.size))

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
        myDomino.setValue()
        myDomino.setSize()
        myDomino.draw()

    elif event.char == "d":
        t.delete(1.0, END)
        newVal = myDomino.randomize()
        sValue.set(value=newVal)
        myDomino.setSize()
        myDomino.setOrientation()
        myDomino.setFace()
        myDomino.draw()
        t.insert(END, "Value: " + str(myDomino.value) + " ")
        t.insert(END, "\n" + "Size: " + str(myDomino.size))
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
mainWindow.config(menu=menubar, bg="steelblue", width= 1080, height = 471)

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

#Display Dominos Canvas
c = Canvas(mainWindow, highlightthickness = 4, highlightbackground="black", bg="white", width=783, height=425)
c.place(x=242, y=25)
c.bind("<Key>", keyPressed)
c.focus_set()

#=======================================================
#Input Box
Frame(mainWindow, highlightthickness = 4, highlightbackground="black", bg= "white", height = 220, width =175).place(x=25, y=55)
Label(mainWindow, bg="steelblue", fg="white", font=("Times, bold", 18), text="Dominos").place(x=65, y=15)
Label(mainWindow, bg="white", fg="black", font=("Times", 14), text="Enter value: ").place(x=30, y=60)
valEntry = Entry(mainWindow, textvariable=sValue, width=10, relief = "solid")
valEntry.place(x=125, y=63)


#Size scale
Label(mainWindow, bg="white", fg="black", text="Size: ", font=("Times", 14)).place(x=30, y=90)
sizeScale = Scale(mainWindow, from_=30, to=100, bg="black", fg="white", orient=HORIZONTAL, command=lambda x: changeSize())
sizeScale.place(x=80, y=90)

#Buttons
Button(mainWindow, text="Proceed", font=("Times bold", 12), bg="steelblue", fg="white", relief = "solid", command=lambda:(mainProgram())).place(x=78, y=139)
Button(mainWindow, text="Clear", font=("Times bold", 12), bg="steelblue", fg="white", relief = "solid", width=6, command=lambda:(clear())).place(x=80, y=180)
Button(mainWindow, text="Randomize", font=("Times bold", 12), bg="steelblue", fg="white", relief = "solid", command=lambda:(goRandomize())).place(x=68, y=225)

#Text 
t = Text(mainWindow,height=2, highlightthickness=3, highlightbackground="black", width=21,bg="white",fg="black", relief = "solid")
t.place(x=25, y= 287)
t.tag_remove(SEL,"1.0", END)

#Below Text Labels
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'D' to draw a random domino!").place(x=5, y= 335)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'F' to increase domino's size!").place(x=5, y= 355)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'G' to decrease domino's size!").place(x=5, y= 375)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'C' to clear the canvas!").place(x=5, y= 395)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'V' to change domino's color!").place(x=5, y= 415)
Label(mainWindow, fg="white", bg="steelblue", font=("Times", 12), text="Press 'X' to exit the program!").place(x=5, y= 435)
#========================================================


mainloop()



