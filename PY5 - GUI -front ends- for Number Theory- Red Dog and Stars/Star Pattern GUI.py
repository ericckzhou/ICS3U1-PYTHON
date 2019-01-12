#Author: Eric Zhou
#Date: Oct 31, 2017
#Purpose: Generating shapes with star patterns with GUI
#Input: Keyboard
#Outputs: Screen/Console
#==================================================

from tkinter import *
#==================================================
#Author: Eric Zhou
#Date: Oct 31, 2017
#Purpose: Generating squares
#Input: size
#Outputs: Screen
#==================================================
def square(size):
    sizeCount = 0
    star = '* '
    while sizeCount != size:
        for count in range(size):
            shapeShow.insert(END,star)
        shapeShow.insert(END,"\n")
        sizeCount += 1
#==================================================
#Author: Eric Zhou
#Date: Oct 31, 2017
#Purpose: Generating hollow squares
#Input: size
#Outputs: Screen
#==================================================
def hSquare(size):
    stars = "* "
    hollow = "  "
    for count in range(1, size + 1):
        shapeShow.insert(END,stars)
    shapeShow.insert(END,"\n")
    for count in range(1, size - 1):
        shapeShow.insert(END,stars)
        for count in range(1, size - 1):
            shapeShow.insert(END, hollow)
        shapeShow.insert(END, stars)
        shapeShow.insert(END,"\n")
    for count in range(1, size + 1):
        shapeShow.insert(END,stars)
#==================================================
#Author: Eric Zhou
#Date: Oct 31, 2017
#Purpose: Generating triangle
#Input: size
#Outputs: Screen
#==================================================
def triangle(size):
    sizeCount = 0
    while sizeCount != size:
        star = '* '
        
        for count in range(sizeCount +1):
            shapeShow.insert(END,star)
        shapeShow.insert(END,"\n")
        sizeCount += 1
#==================================================
#Author: Eric Zhou
#Date: Oct 31, 2017
#Purpose: Generating hollow triangle
#Input: size
#Outputs: Screen
#==================================================
def hTriangle(size):
    stars = "* "
    hollow = "  "
    
    if (size == 1 or size == 2):
        for count in range(1, size + 1):
            for count in range(1, count + 1):
                shapeShow.insert(END,stars)
            shapeShow.insert(END,"\n")
            
    elif (size > 2):
        for count in range(1, 3):
            for count in range(1, count + 1):
                shapeShow.insert(END,stars)
            shapeShow.insert(END,"\n")
            
        for count in range(1, size - 2):
            shapeShow.insert(END,stars)
            for count in range(1, count + 1):
                shapeShow.insert(END,hollow)
            shapeShow.insert(END, stars)
            shapeShow.insert(END,"\n")
            
        for count in range(1, size + 1):
            shapeShow.insert(END,stars)

        shapeShow.insert(END,"\n")
#==================================================
#Author: Eric Zhou
#Date: Oct 31, 2017
#Purpose: When button clicked to proceed, it decides which program to run!
#Input: size, check shape you want
#Outputs: Screen
#==================================================
def runProgram():
    shape = int(shapeX.get())
    sSize = int(size.get())
    useHollow= int(hollow.get())
    valid = True
    if not (shape in range(1,3) or useHollow in range(1,3)):
        messagebox.showerror("Error", "You must select a shape and solid or hollow!")
    if shape == 1 and useHollow == 1 and valid == True :
        square(sSize)
    if shape == 1 and useHollow == 2 and valid == True:
        hSquare(sSize)
        
    if shape == 2 and useHollow == 1 and valid == True:
        triangle(sSize)
    if shape == 2 and useHollow == 2 and valid == True:
        hTriangle(sSize)
#==================================================
#Author: Eric Zhou
#Date: Oct 31, 2017
#Purpose: clears the textbox
#Input: Clears textbox
#Outputs: Screen
#==================================================
def clear():
    shapeShow.delete(1.0,END)
    

    
    
mainWindow = Tk()
mainWindow.title("Star Patterns")
size = IntVar()
display = StringVar()
hollow = IntVar()
menubar = Menu(mainWindow)
shapeX = IntVar()



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

userInput = StringVar()
hollowButton = IntVar()

mainWindow.config(menu=menubar, bg = "white", width=500, height = 300)

Label(mainWindow, text="Choose your shape: ", font=("Arial",12), bg = "white", fg ="black").place(x=10,y=10) 

Radiobutton(mainWindow, text="Square", fg="black", font=("Arial",10), bg="white", value = 1, variable=shapeX).place(x=10,y=35)
Radiobutton(mainWindow, text="Triangle", fg="black", font=("Arial",10), bg="white", value = 2, variable=shapeX).place(x=10,y=65)
Radiobutton(mainWindow, text="Solid", fg="black", font=("Arial",10), bg="white", value = 1, variable=hollow).place(x=10,y=95)
Radiobutton(mainWindow, text="Hollow", fg="black", font=("Arial",10), bg="white", value = 2, variable=hollow).place(x=10,y=125)

Label(mainWindow, text="Size: ", fg="black", bg="white", font=("Arial",10)).place(x=15, y=153)
size = Scale(mainWindow, from_=1, to=15, orient=HORIZONTAL)
size.place(x=15, y=173)

Frame(mainWindow, highlightthickness = 4, highlightbackground="black", bg = "steelblue", width=322, height=279).place(x=163,y=15)

shapeShow = Text(mainWindow,height=16, width=37, relief = "solid")
shapeShow.place(x=174,y=25)


Button(mainWindow, text="Proceed", fg="black", font=("Arial",12), bg="white", command=lambda:runProgram()).place(x=10, y=223)
Button(mainWindow, text="Clear", fg="black", font=("Arial",12), bg="white", command=lambda:clear()).place(x=10, y=260)

Button(mainWindow, text="Exit", fg="black", font=("Arial",12), bg="white", command=lambda:mainWindow.destroy()).place(x=75, y=260)




mainloop()



