 #============================================================================
#Date: 1/8/2018
#Author: Eric Zhou
#Purpose: Experiment with integer lists class
#Inputs: N/A
#Outputs: Screen/Monitor
#============================================================================

import random
from tkinter import *

#============================================================================
#Date: 1/8/2018
#Author: Eric Zhou
#Purpose: To hold and organize multiple integers
#Inputs: N/A
#Outputs: N/A
#Methods ====================================================================
#__init__:     Constructs the class.
#__str__:      Return the list flowed by the size.
#initAsNum:    Recreates the list with a given parameter value, given the size.
#initAsSeq:    Recreates the list with the values.
#calcTotal:    Return the total value of the elements in the list.
#calcMean:     Returns the averagest of the element in the list.
#findLargest:  Returns the largest element in list.
#calcFreq:     Returns a count of the number of elements matching a given parameter value in the list.
#insertAt:     Inserts a given value into the IntGroup at a given position.
#removeAt:     Removes the element at a given parameter position in list.
#removeAll:    Removes all elements in list matching a given parameter value.
#findFirst:    Returns the position of a given parameter value element in list.
#isSorted:     Returns true if list is in ascending order.
#merge:        Returns an IntGroup Object which is the result of merging the current intGroup and another.
#============================================================================
class IntGroup:
    def __init__(self, intList = [], size=0):
        self.intList = intList
        self.size = size
        if (size >=0) and (size <=20):
            for i in range(self.size):
                self.intList.append(random.randint(0, self.size))
            
#============================================================================
#Date: 1/8/2018
#Author: Eric Zhou
#Purpose: Return the list flowed by the size.
#Inputs: Self
#Outputs: Size list
#============================================================================
    def __str__(self):
        return str(self.intList) + ' ' + 'Size: ' + str(self.size)
    
#============================================================================
#Date: 1/9/2018
#Author: Eric Zhou
#Purpose: Recreates the list with a given parameter value, given the size.
#Inputs: Self, givenValue
#Outputs: N/A
#============================================================================
    def initAsNum(self, value, givenSize):
        self.intList = []
        self.size = givenSize
        for i in range(givenSize):
            self.intList.append(value)
        
#============================================================================
#Date: 1/9/2018
#Author: Eric Zhou
#Purpose: Recreates the list with the values.
#Inputs: Self, givenValue
#Outputs: N/A
#============================================================================
    def initAsSeq(self, givenSize):
        self.intList = []
        self.size = givenSize
        for i in range(1, self.size +1):
            self.intList.append(i)

#============================================================================
#Date: 1/9/2018
#Author: Eric Zhou
#Purpose: Return the total value of the elements in the list.
#Inputs: Self
#Outputs: Sum of elements
#============================================================================
    def calcTotal(self):
        totalSum = 0
        for i in self.intList:
            totalSum += i
        return totalSum

#============================================================================
#Date: 1/9/2018
#Author: Eric Zhou
#Purpose:Returns the averagest of the element in the list.
#Inputs: Self
#Outputs: Average
#============================================================================
    def calcMean(self):
        getTotalSum = self.calcTotal()
        elements = len(self.intList)
        if elements == 0 or getTotalSum == 0:
            average = 0
        else:
            average = getTotalSum // elements
        return average

#============================================================================
#Date: 1/9/2018
#Author: Eric Zhou
#Purpose: Returns the largest element in list
#Inputs: Self
#Outputs: Return largest element
#============================================================================
    def findLargest(self):
        largest = 0
        if not len(self.intList) == 0:
            largest += max(self.intList)
        return largest

#============================================================================
#Date: 1/9/2018
#Author: Eric Zhou
#Purpose: Returns a count of the number of elements matching a given parameter value in the list.
#Inputs: Self, givenValue
#Outputs: Return matching elements
#============================================================================
    def calcFreq(self, givenValue):
        count = 0
        if givenValue in self.intList:
            count = self.intList.count(givenValue)
        return count
    
#============================================================================
#Date: 1/9/2018
#Author: Eric Zhou
#Purpose: Inserts a given value into the IntGroup at a given position.
#Inputs: Self, givenValue, position
#Outputs: N/A
#============================================================================    
    def insertAt(self, givenValue, position):
        if position < 0:
            position = 0
        if position > len(self.intList):
            position = len(self.intList)
        self.intList.insert(position, givenValue)
        
#============================================================================
#Date: 1/9/2018
#Author: Eric Zhou
#Purpose: Removes the element at a given parameter position in list.
#Inputs: Self, position
#Outputs: N/A
#============================================================================
    def removeAt(self, position):
        size = int(sizeScale.get())
        if not position in range(0, size):
            position = 0
            userValue.set(value=0)
            messagebox.showerror("Error", "The entered position is not in list range!")
            
        if self.intList[position] in self.intList and position in range(len(a.intList)):
            del self.intList[position]
            sizeScale.set(value=(size-1))

                
#============================================================================
#Date: 1/9/2018
#Author: Eric Zhou
#Purpose: Removes all elements in list matching a given parameter value.
#Inputs: Self, givenValue
#Outputs: N/A
#============================================================================
    def removeAll(self, givenValue):
        for i in self.intList:
            if givenValue == i:
                self.intList.remove(i)
                sizeScale.set(value=(len(a.intList)))

    
#============================================================================
#Date: 1/9/2018
#Author: Eric Zhou
#Purpose: Returns the position of a given parameter value element in the list.
#Inputs: Self, given Value
#Outputs: Position
#============================================================================
    def findFirst(self, givenValue):
        if int(givenValue) in self.intList:
            position = self.intList.index(int(givenValue))
        else:
            position = -1
            
        return position
    
#============================================================================
#Date: 1/10/2018
#Author: Eric Zhou
#Purpose: Returns true if list is in ascending order.
#Inputs: Self
#Outputs: valid
#============================================================================
    def isSorted(self):
        valid = "True"
        for i in range(len(self.intList) - 1):
            if not self.intList[i] <= self.intList[i+1]:
                valid = "False"
            
        return valid
#============================================================================
#Date: 1/10/2018
#Author: Eric Zhou
#Purpose: Returns an IntGroup Object which is the result of merging the current intGroup and another.
#Inputs: Self
#Outputs: New merged list
#============================================================================
    def merge(self, IntGroup):
        ig = IntGroup
        c = []

        while not (len(self.intList) == 0 or len(ig.intList) == 0):
            if min(self.intList) <= min(ig.intList):
                c.append(min(self.intList))
                self.intList.remove(min(self.intList))
            else:
                c.append(min(ig.intList))
                ig.intList.remove(min(ig.intList))
                
        while not (len(self.intList)) == 0:
            c.append(min(self.intList))
            self.intList.remove(min(self.intList))
            
        while not (len(ig.intList)) == 0:
            c.append(min(ig.intList))
            ig.intList.remove(min(ig.intList))
            
        return c


#============================================================================
#Date: 1/12/2018
#Author: Eric Zhou
#Purpose: To perform user desire actions to list in initialize section.
#Inputs: N/A
#Outputs: N/A
#============================================================================
def userClickedInitialize():
    t.delete(1.0, END)
    initState = str(initialize.get())
    if not initState.isdigit():
        initState = 0
    else:
        initState = int(initialize.get())
        
    a.size = int(sizeScale.get())
    
    initVal = str(initValue.get())
    if not initVal.isdigit():
        initVal = 0
        initValue.set(value=0)
    else:
        initVal = int(initValue.get())
        
    if initState == 2:
        lista = a.initAsSeq(a.size)
    else:
        lista = a.initAsNum(initVal, a.size)
        
    t.insert(END, a.intList)
    
    guiFeatureText()    
#============================================================================
#Date: 1/12/2018
#Author: Eric Zhou
#Purpose: To perform user desire actions to list in Other Features section
#Inputs: N/A
#Outputs: N/A
#============================================================================       
def userClickedProceed():
    t.delete(1.0, END)
    valFeature = str(feature.get())
    value = str(userValue.get())
    position = str(userPos.get())
    size = int(sizeScale.get())
    valFeature = int(feature.get())
        
    if not(value.isdigit()):
        value = 0
        userValue.set(value=0)
    else:
        value = int(userValue.get())
    if not position.isdigit():
        position = 0
        userPos.set(value=0)
    else:
        position=int(userPos.get())
        
    val = 0
    firstNum = 0

    if valFeature == 1 and size > len(a.intList):
        a.insertAt(value, position)
    elif valFeature == 1 and size <= len(a.intList):
        messagebox.showerror("Error", "You cannot exceed the size limit!")
    elif valFeature == 2:
        a.intList = []
        b.intList = []
        for i in range(size):
           a.intList.append(random.randint(0, size))
           b.intList.append(random.randint(0, size))
        saveA = []
        saveB = []
        saveA.append(a.intList[:])
        saveB.append(b.intList[:])
        c.intList = a.merge(b)
        
    elif valFeature == 3 and len(a.intList) > 0:
        a.removeAt(position)
    elif valFeature == 4 and len(a.intList) > 0:
        a.removeAll(value)
    elif (valFeature == 4 or valFeature == 3) and len(a.intList) == 0:
        messagebox.showerror("Error", "There is nothing in the list!")

    if valFeature != 2:
        t.insert(END, a.intList)
        
    if valFeature == 2:
        t.insert(END, saveA[:])
        t.insert(END, " + ")
        t.insert(END, saveB[:])
        t.insert(END, " = ")
        t.insert(END, c.intList[:])
        
    guiFeatureText()
    
#============================================================================
#Date: 1/12/2018
#Author: Eric Zhou
#Purpose: Adds text to the feature textbox.
#Inputs: N/A
#Outputs: N/A
#============================================================================
def guiFeatureText():
    ft.delete(1.0, END)
    if not str(userValue.get()).isdigit():
        userValue.set(value=0)
    if not str(userPos.get()).isdigit():
        userPos.set(value=0)
    ft.insert(END, "Size = " + str(sizeScale.get()))
    ft.insert(END, "\n" + "Total = " + str(a.calcTotal()))
    ft.insert(END, "\n" + "Mean = " + str(a.calcMean()))
    ft.insert(END, "\n" + "Largest = " + str(a.findLargest()))
    ft.insert(END, "\n" + "Sorted = " + str(a.isSorted()))
    ft.insert(END, "\n" + "Freq = " + str(a.calcFreq(int(userValue.get()))))
    if int(feature.get()) != 2:
        ft.insert(END, "\n" + "findFirst = " + str(a.findFirst(userValue.get())))
    else:
        ft.insert(END, "\n" + "findFirst = " + str(c.findFirst(userValue.get())))
#============================================================================
#Date: 1/12/2018
#Author: Eric Zhou
#Purpose: Clears all textboxes
#Inputs: N/A
#Outputs: N/A
#============================================================================
def clear():
    t.delete(1.0, END)
    ft.delete(1.0, END)
    a.intList = []
    b.intList = []
    c.intList = []
#============================================================================
#Date: 1/12/2018
#Author: Eric Zhou
#Purpose: Randomizes the list
#Inputs: N/A
#Outputs: N/A
#============================================================================
def randomize():
    clear()
    size = int(sizeScale.get())
    
    for i in range(size):
        a.intList.append(random.randint(0, size))

    t.insert(END, a.intList)
    
    guiFeatureText()
    
mainWindow = Tk()  
mainWindow.title("IntGroups - Lists")

#StringVars
initialize = StringVar()
initialize.set(value="1")
initValue = StringVar()
initValue.set(value="0")
fntclr = "black"
bgclr = "white"
feature = StringVar()
feature.set(value=1)
userValue = StringVar()
userValue.set(value="0")
userPos = StringVar()
userPos.set(value="0")

global a
a = IntGroup()

global b
b = IntGroup()

global c
c = IntGroup()

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
mainWindow.config(menu=menubar, bg=bgclr, width= 430, height = 375)

#textbox
t = Text(mainWindow, height=6, width=49, relief="solid", bg=bgclr, fg=fntclr , highlightbackground="black", highlightthickness="2")
t.place(x=15,y=15)

#Under sizescale
sizeScale = Scale(mainWindow, from_=0, to =20, length=75, width=22, bg=bgclr, fg=fntclr, font=("Times", 12, "bold"), orient=HORIZONTAL, command=lambda x:guiFeatureText())
sizeScale.place(x=15, y=150)
Label(mainWindow, bg=bgclr, fg=fntclr , text="Size Scale", font=("Times", 12, "bold", "underline")).place(x=15, y=120)
Button(mainWindow, text="CLEAR", font=("Tim es", 10, "bold"), width=10, relief="solid", fg=fntclr, bg=bgclr, command=lambda:clear()).place(x=15, y=210)

#Under INITIALIZING AS...
Label(mainWindow, bg=bgclr, fg=fntclr, text=" Initalizing As ... ", font=("Times", 12, "bold", "underline")).place(x=110, y=120)
initEntry = Entry(mainWindow, textvariable= initValue, width=5, relief="solid")
initEntry.place(x=192, y=155)
Radiobutton(mainWindow, text="Number", font=("Times", 12), value=1, variable=initialize, fg=fntclr, bg=bgclr, command=lambda:initEntry.config(state="normal")).place(x=105, y=150)
Radiobutton(mainWindow, text="Sequence",font=("Times", 12), value=2, variable=initialize, fg=fntclr, bg=bgclr, command=lambda:initEntry.config(state="disabled")).place(x=105, y=175)
Button(mainWindow, text=" INITIALIZE ", font=("Times", 10, "bold"), width=15, relief="solid", fg=fntclr, bg=bgclr, command=lambda:userClickedInitialize()).place(x=110, y=210)

#Under Other Features...
Label(mainWindow, bg=bgclr, fg=fntclr, text="      Other Features ...      ", font=("Times", 12, "bold", "underline")).place(x=240, y=120)
valueEntry = Entry(mainWindow, textvariable= userValue, width=5, relief="solid")
valueEntry.place(x=283, y=250)
Label(mainWindow, bg=bgclr, fg=fntclr, text="Position", font=("Times", 12)).place(x=320, y= 247)
posEntry = Entry(mainWindow, textvariable= userPos, width=5, relief="solid")
posEntry.place(x= 377, y=250)
Radiobutton(mainWindow, text="insertAt", font=("Times", 12), value=1, variable=feature, fg=fntclr, bg=bgclr, command=lambda:(valueEntry.config(state="normal"), posEntry.config(state="normal"))).place(x=270, y=150)
Radiobutton(mainWindow, text="removeAt",font=("Times", 12), value=3, variable=feature, fg=fntclr, bg=bgclr, command=lambda:(valueEntry.config(state="disabled"), posEntry.config(state="normal"))).place(x=270, y=194)
Radiobutton(mainWindow, text="removeAll", font=("Times", 12), value=4, variable=feature, fg=fntclr, bg=bgclr, command=lambda:(valueEntry.config(state="normal"), posEntry.config(state="disabled"))).place(x=270, y=216)
#If it's set at merge, check button for findFirst finds the newly created list.
Radiobutton(mainWindow, text="merge", font=("Times", 12), value=2, variable=feature, fg=fntclr, bg=bgclr, command=lambda:(valueEntry.config(state="normal"), posEntry.config(state="disabled"))).place(x=270, y=172)


Label(mainWindow, bg=bgclr, fg=fntclr, text="Value", font=("Times", 12)).place(x=240, y= 247)
Button(mainWindow, text=" PROCEED ", font=("Times", 10, "bold"), width=23, relief="solid", fg=fntclr, bg=bgclr, command=lambda:userClickedProceed()).place(x=240, y=275)
Button(mainWindow, text="  RANDOM LIST ", font=("Times", 10, "bold"), width=23, relief="solid", fg=fntclr, bg=bgclr, command=lambda:randomize()).place(x=240, y=305)
Button(mainWindow, text="  CHECK LIST  ", font=("Times", 10, "bold"), width=23, relief="solid", fg=fntclr, bg=bgclr, command=lambda:guiFeatureText()).place(x=240, y=335)

#Features Textbox of List eg. seeing if list is sorted, sorted =true/false etc
ft = Text(mainWindow, height=7, width=25, relief="solid", bg=bgclr, fg=fntclr , highlightbackground="black", highlightthickness="2")
ft.place(x=15,y=243)

mainloop()
        
