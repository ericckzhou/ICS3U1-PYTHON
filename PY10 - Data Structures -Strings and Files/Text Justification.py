#=======================================================================================================
#Author: Eric Zhou
#Date: 1/15/2018
#Purpose: Experimenting with Justification Text Class.
#Inputs: N/A
#Outputs: Screen/Monitor
#========================================================================================================

#========================================================================================================
#Author: Eric Zhou
#Date: 1/15/2018
#Purpose: To create text, justified either left, right or full.
#Inputs: N/A
#Outputs: Screen/Monitor
#Data Elements ==========================================================================================
#wordsList:        A list that holds the words of the file.
#docList:          A list that holds the lines of justified text.
#strInputFile:     A string containing the input text file name.
#strOutputFile:    A string containing the output text file name.
#strJustification: This strings indicates if the text will be 'l', 'r', or 'c' (left, right, centre).
#intWidth:         This contains the column width from 30 - 90.
#Methods ================================================================================================
#__init__:         Constructs the class.
#readFile:         Reads the file and creates the words list.
#writeFile:        Writes the docList formatted as defined by parameters to the object.
#createDoc:        Call justify Left or Right, or Centre or Full dependent on data field settings.
#justifyLeft:      Make the text left justified.
#justifyRight:     Call justifyLeft and add require spaces to front of each line for desire results.
#justifyCentre:    Call justifyLeft and add require spaces to front of each line for desire results.
#__str__:          Concatenates the lines of text from the doc list(with '\n'; new line)
#========================================================================================================

class JustifyText:
    def __init__(self, strInputFile="input.txt", strOutputFile= "output.txt", strJustification="l", intWidth=60):
        self.wordsList = []
        self.docList = []
        if len(strInputFile) == 0:
            print("Your input file is empty!")
        self.strInputFile = strInputFile
        self.strOutputFile = strOutputFile
        
        if not (strJustification == "l" or strJustification =="r" or strJustification == "c"):
            print("Your justification is not valid, auto set to 'l'!")
            self.strJustification = "l"
        else:
            self.strJustification = strJustification
            
        if not str(intWidth).isdigit():
            print("Your width is not an integer! Auto set to 60.")
            self.intWidth = 60
            
        if not (int(intWidth) in range(30, 91)):
            print("Your width is not in range 30 to 90! Auto set to 60.")
            self.intWidth = 60
        else:
            self.intWidth = int(intWidth)
            
        
#==================================================================
#Author: Eric Zhou
#Date: 1/16/2018
#Purpose: Reads the file and creates the words list.
#Inputs: N/A
#Outputs: N/A
#==================================================================
        
    def readFile(self):
        inputFile = open(self.strInputFile, 'r')
        for line in inputFile:
            tempWordList = line.strip().split()
            for strWord in tempWordList:
                if len(strWord) > 30:
                    strWord = strWord[:30]
                self.wordsList.append(strWord+" ")       
        inputFile.close()
        
#==================================================================
#Author: Eric Zhou
#Date: 1/16/2018
#Purpose: Writes the docList formatted as defined by parameters to the object.
#Inputs: N/A
#Outputs: N/A
#==================================================================
        
    def writeFile(self):
        outputFile = open(self.strOutputFile, 'w')
        outputFile.write(self.__str__())
        outputFile.close()

#==================================================================
#Author: Eric Zhou
#Date: 1/16/2018
#Purpose: Call justify Left or Right, or Centre or Full dependent on data field settings.
#Inputs: N/A
#Outputs: N/A
#==================================================================

    def createDoc(self):
        if self.strJustification == "l":
            self.justifyLeft()
        elif self.strJustification == "r":
            self.justifyRight()
        elif self.strJustification == "c":
            self.justifyCentre()
            
#==================================================================
#Author: Eric Zhou
#Date: 1/17/2018
#Purpose: Make the text left justified.
#Inputs: N/A
#Outputs: N/A
#==================================================================
            
    def justifyLeft(self):
        inputFile = open(self.strInputFile, 'r')
        localLine = ""
        for line in inputFile:
            tempWordList = line.strip().split()
            
            for strWord in tempWordList:
                if (len(strWord) + len(localLine)) +1 <= self.intWidth:
                    localLine += str(strWord) + ' '
                else:
                    self.docList.append(localLine)
                    localLine = str(strWord) + ' '
                    
        if len(localLine) > 0:
            self.docList.append(localLine)
            
        inputFile.close()
            

#==================================================================
#Author: Eric Zhou
#Date: 1/18/2018
#Purpose: Make the text right justified.
#Inputs: N/A
#Outputs: N/A
#==================================================================       
    def justifyRight(self):
        self.justifyLeft()
        tempList = []
        for line in self.docList:
            localLine = ""
            if not len(line) == self.intWidth:
                space = ' ' * (self.intWidth - len(line))
                localLine += str(space) + str(line)
                tempList.append(localLine)
            else:
                tempList.append(line)

        self.docList = tempList
#==================================================================
#Author: Eric Zhou
#Date: 1/18/2018
#Purpose: Make the text centred justified.
#Inputs: N/A
#Outputs: N/A
#==================================================================            
    def justifyCentre(self):
        self.justifyLeft()
        tempList = []
        for line in self.docList:
            localLine = ""
            if not len(line) == self.intWidth:
                space = ' ' * ((self.intWidth - len(line)) // 2)
                localLine += str(space) + str(line) + str(space)
                tempList.append(localLine)
            else:
                tempList.append(line)
                
        self.docList = tempList

#==================================================================
#Author: Eric Zhou
#Date: 1/18/2018
#Purpose: Creates a new line from docList with '\n'.
#Inputs: N/A
#Outputs: N/A
#==================================================================            
    def __str__(self):
        for line in self.docList:
            return ('\n'.join(self.docList))

            

#MAIN CODE
justification = input("What justification do you want? 'l', 'r' or 'c' :")
width = input("Enter a width for the text! 30 - 90: ")
yourText = JustifyText("input.txt", "output.txt", justification, width)
yourText.readFile()
yourText.createDoc()
yourText.writeFile()
print("Check your output file!")

y = True
while y == True:
    tryAgain = input("Do you want to rerun this program? Y/N : ")
    if tryAgain == "n" or tryAgain == "N":
        y = False
    else:
        justification = input("What justification do you want? 'l', 'r' or 'c' :")
        width = input("Enter a width for the text! 30 - 90: ")
        yourText = JustifyText("input.txt", "output.txt", justification, width)
        yourText.readFile()
        yourText.createDoc()
        yourText.writeFile()
        print("Check your output file!")
