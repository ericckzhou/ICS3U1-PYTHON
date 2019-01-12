#============================================
#Author: Eric Zhou :) 
#Purpose: Create A GUI version off Red Dog
#Date: Oct 31, 2017
#Inputs: Keyboard, bet
#Output: game status, wins, loss, draws, etc
#============================================
from tkinter import *
import math
import random
#============================================
#Author: Eric Zhou :) 
#Purpose: Class getting 2 cards
#Date: Oct 18, 2017
#Inputs: Keyboard, card1, card2
#Output: None
#============================================
class TwoCards:
    def __init__ (self, card1, card2):
        self.card1 = card1
        self.card2 = card2

#==============================================================        
#Sub Programs
#Author: Eric Zhou :) 
#Purpose: Getting a card between 2 and 14 and return the card
#Date: Oct 18, 2017
#Input: Keyboard
#Outputs: a card with the value between 2-14
#==============================================================
def getCard():
    card = random.randint(2,14)
    return card

#=============================================================
#Author: Eric Zhou :) 
#Purpose: Getting a hand of a TwoCards Object and returning it
#Date: Oct 16, 2017
#Inputs: Keyboard
#Output: Hand
#=============================================================
def getHand():
    hand = TwoCards(getCard(),getCard())
    return hand

#============================================
#Author: Eric Zhou :) 
#Purpose: Getting the number of card
#Date: Oct 18, 2017
#Inputs: Keyboard, value of the card
#Outputs: Word of the number of the card
#============================================
def getStrCard(card):
    if card == 2:
        strCard = "2"
    if card == 3:
        strCard = "3"
    if card == 4:
        strCard = "4"
    if card == 5:
        strCard = "5"
    if card == 6:
        strCard = "6"
    if card == 7:
        strCard = "7"
    if card == 8:
        strCard = "8"
    if card == 9:
        strCard = "9"
    if card == 10:
        strCard = "10"
    if card == 11:
        strCard = "11"
    if card == 12:
        strCard = "12"
    if card == 13:
        strCard = "13"
    if card == 14:
        strCard = "1"
        
    return strCard

#==================================================================
#Author: Eric Zhou :) 
#Purpose: Giving the word number of that card type
#Date: Oct 18, 2017
#Inputs: Word of the number of the card, keyboard
#Outputs: Returns the word of the number of the card plus the suit
#==================================================================
def getCardSuit():

    cardSuit = random.randint(1,4)
    if cardSuit == 1:
        suitCard = "♠"
        
    if cardSuit == 2:
        suitCard = "♥"
        
    if cardSuit == 3:
        suitCard = "♣"
        
    if cardSuit == 4:
        suitCard = "♦"
    cardSuit =0
    return suitCard

#=======================================================
#Author: Eric Zhou :)
#Purpose: To find out what type of hand is the player's
#Date: Oct 18, 2017
#Inputs: hand, keyboard
#Outputs: handType
#=======================================================
def getHandType(hand):
    card1 = hand.card1
    card2 = hand.card2
    handType = ""
    if card1 +1 == card2 or card1 -1 == card2:
        handType += "Consecutive"
    if card1 == card2:
        handType += "Pair"
    if handType != "Consecutive" and handType != "Pair":
        handType += "Non-Consecutive"
    return handType

#===============================================
#Author: Eric Zhou :)
#Purpose: Getting the spread from player's hand
#Date: Oct 18, 2017
#Inputs: hand, keyboard
#Outputs: spread
#===============================================
def getSpread(hand):
    card1 = hand.card1
    card2 = hand.card2
    if card1 > card2:
        spread = card1 - card2 - 1
        
    if card2 > card1:
        spread = card2 - card1 - 1

    if card1 == card2:
        spread = 0 
    return spread

#================================================================
#Author: Eric Zhou :)
#Purpose: Calculating the payout from spread and returning payout
#Date: Oct 18, 2017
#Inputs: Spread, keyboard
#Outputs: Payout
#================================================================
def getPayout(spread):
    payout = 1
    if spread <3 and spread >0:
        payout = 6
        for i in range(spread):
            payout -= 1
    if spread >3:
       payout = 1
    if spread == 0:
        payout = 1
        
    return payout

#=========================================================
#Author: Eric Zhou :)
#Purpose: Confirming whether or not card3 is between hand
#Date: Oct 18, 2017
#Inputs: Hand and card3, keyboard
#Outputs: between True or False
#=========================================================

def ifBetween(hand, card3):
    card1 = hand.card1
    card2 = hand.card2
    if card3 > card1 and card3 < card2 or card3 > card2 and card3 < card1:
        between = "True"
    else:
        between = "False"
    return between

#=========================================================
#Author: Eric Zhou :)
#Purpose: Confirming whether bet is valid
#Date: Oct 29, 2017
#Inputs: Bet
#Outputs: Returns bet to redDog sub program
#=========================================================
def userClickedBet():
    valid = True
    strBet = str(bet.get())
    if str(validFirstBet.get()) == "True" and str(validAddBet.get())=="False":
        messagebox.showerror("Error", "You must restart game to play again!")
        valid =False

    if str(validAddBet.get()) == "False" and valid == True:
        messagebox.showerror("Error", "You cannot make an additional bet")
        valid = False
    
    if str(validFirstBet.get()) == "True" and valid == True:
        messagebox.showerror("Error", "You must make an additional bet or pass!")
        valid = False
    if not strBet.isdigit() and valid == True:
        messagebox.showerror("Error", "You did not input any positive valid integers")
        valid = False
    if valid == True:
        intBet = int(bet.get())
        intBalance = int(balance.get())
        if intBet > intBalance  or intBet <0:
            messagebox.showerror("Error", "Your last inputs were not in range of 1 -" + str(intBalance))
            valid = False
            
        if valid == True:
            validFirstBet.set(value="True")
            firstBet.set(value=intBet)
            playRedDog()

#=========================================================
#Author: Eric Zhou :)
#Purpose: If Non-Consecutive hand is true, player decides on additional bet
#Date: Oct 29, 2017
#Inputs: Additional Bet
#Outputs: Returns additional bet to nonconsecutive sub program
#=========================================================
            
def userClickedAddBet():
    valid = True
    strAddBet = str(bet.get())

    if str(validFirstBet.get()) == "True" and str(validAddBet.get())=="False":
        messagebox.showerror("Error", "You must restart game to play again!")
        valid =False

    intBalance = int(balance.get())
    if intBalance == 0 and valid == True:
        messagebox.showerror("Error", "You do not have money to make an additional bet! Please click pass bet!")
        valid = False

    if str(validFirstBet.get()) == "False" and valid == True:
        messagebox.showerror("Error", "You cannot make an additional bet yet")
        valid = False
        
    if str(validAddBet.get()) == "False" and valid == True:
        messagebox.showerror("Error", "You cannot make an additional bet!")
        valid = False
        
    if not strAddBet.isdigit() and valid == True:
        messagebox.showerror("Error", "You did not input any positive valid integers")
        valid = False
        
    if valid == True:
        intAddBet = int(bet.get())
        intBet = int(firstBet.get())
        intBalance = int(balance.get())

        if intAddBet <0 or intAddBet > intBet:
            messagebox.showerror("Error", "Your last inputs were not in range of 1 - " + str(intBet))
            valid = False
            
        if intAddBet <0 or intAddBet > intBalance and valid == True:
            messagebox.showerror("Error", "Your last inputs were not in range of 1 - " + str(intBalance))
            valid = False
            
        if valid == True:
            payment = intBalance - intAddBet
            validAddBet.set(value="False")
            balance.set(value=str(payment))
            displayBalance.set(value="$"+ str(balance.get()))
            additionalBet.set(value=(bet.get()))
            NonConsecutive()
            
#=========================================================
#Author: Eric Zhou :)
#Purpose: Confirming whether card3 is between or not after getting additional bet
#Date: Oct 29, 2017
#Inputs: Additional Bet
#Outputs: Returns messageboxes and payment whether player lost or won
#=========================================================    

def NonConsecutive():
    intBalance = int(balance.get())
    intBet = int(firstBet.get())
    intPayout = int(payout.get())
    intAddBet = int(additionalBet.get())
    strBetween = str(between.get())
    card3.set(value=str(displayCard3.get()))
    suitCard3.set(value=str(displaySuitCard3.get()))
    
    if str(between.get()) == "True":
        gameStatus.set(value="Win")
        displayGameStatus.set(value="Game Status: "+str(gameStatus.get()))
        payment= intBalance + (intAddBet + intBet) * intPayout + intBet + intAddBet
        balance.set(value=str(payment))
        messagebox.showinfo("Won", "The card was between! You won!")
        messagebox.showinfo("Reset Game", "Click Reset Game to play again!")
        displayBalance.set(value="$"+ str(balance.get()))
        storeWins = int(wins.get()) + 1
        wins.set(value= storeWins)
        displayWins.set(value="Wins: "+str(wins.get()))
        storePayment = (intAddBet + intBet) * intPayout
        storingPayment.set(value=storePayment)
        displayPayment.set(value="Payment: +$"+str(storingPayment.get()))

    if str(between.get()) == "False":
        gameStatus.set(value="Lost")
        displayGameStatus.set(value="Game Status: "+str(gameStatus.get()))
        payment= intBalance
        balance.set(value=str(payment))
        messagebox.showerror("Lost", "The card was not between! You lost!")
        messagebox.showinfo("Reset Game", "Click Reset Game to play again!")
        storeLoss = int(loss.get()) + 1
        loss.set(value=storeLoss)
        displayLoss.set(value="Loss: " + str(loss.get()))
        storePayment = intBet + intAddBet
        storingPayment.set(value=storePayment)
        displayPayment.set(value="Payment: -$"+str(storingPayment.get()))
        
#=========================================================
#Author: Eric Zhou :)
#Purpose: If player wants to pass additional bet, additional bet == 0
#Date: Oct 29, 2017
#Inputs: Click
#Outputs: Return additional bet to NonConsecutive sub program
#=========================================================
def userClickedPass():
    valid = True
    if str(validFirstBet.get()) == "False":
        messagebox.showerror("Error", "You cannot pass a bet yet")
        valid = False
        
    if str(validFirstBet.get()) == "True" and str(validAddBet.get())=="False" and valid == True:
        messagebox.showerror("Error", "You must restart game to play again!")
        valid =False

    if valid == True:
        additionalBet.set(value="0")
        validAddBet.set(value="False")
        NonConsecutive()
        
#=========================================================
#Author: Eric Zhou :)
#Purpose: Red Dog game, gets hand, handtype, payout, etc
#Date: Oct 29, 2017
#Inputs: Bet
#Outputs: Stores values needed for later, etc
#=========================================================        
def playRedDog():
    intBet = int(bet.get())
    intBalance = int(balance.get())
    newBalance = intBalance - intBet
    balance.set(value=str(newBalance))
    displayBalance.set(value="$"+ str(balance.get()))
    hand = getHand()
    storeHandType = getHandType(hand)
    handType.set(value=storeHandType)
    displayHandType.set(value="Hand Type: " + str(handType.get()))
    intCard1 = hand.card1
    intCard2 = hand.card2
    strCard1 = getStrCard(intCard1)
    strCard2 = getStrCard(intCard2)
    storeSuitCard1 = getCardSuit()
    storeSuitCard2 = getCardSuit()
    
    while strCard1 == strCard2 and storeSuitCard1 == storeSuitCard2:
        storeSuitCard1 = getCardSuit()

    intCard3 = getCard()
    strCard3 = getStrCard(intCard3)
    storeSuitCard3 = getCardSuit()
    
    while (strCard1 == strCard3 and storeSuitCard1 == storeSuitCard3) or (strCard1 == strCard3 and storeSuitCard2 == storeSuitCard3):
        storeSuitCard3 = getCardSuit()

    storeHandType = getHandType(hand)
    spread = getSpread(hand)
    storePayout = getPayout(spread)
    payout.set(value=storePayout)
    storeBetween = ifBetween(hand, intCard3)
    between.set(value=storeBetween)
    card1.set(value=strCard1)
    card2.set(value=strCard2)
    suitCard1.set(value=storeSuitCard1)
    suitCard2.set(value=storeSuitCard2)

    if storeHandType == "Pair":
        validAddBet.set(value="False")
        card3.set(value=strCard3)
        
        suitCard3.set(value=storeSuitCard3)
        if strCard1 == strCard2 and strCard1 == strCard3:
            gameStatus.set(value="Won")
            displayGameStatus.set(value="Game Status: "+str(gameStatus.get()))
            messagebox.showinfo("Notice", "You won!")
            payment = intBalance + (intBet * 11)
            balance.set(value=str(payment))
            displayBalance.set(value="$"+ str(balance.get()))
            storeWins = int(wins.get()) + 1
            wins.set(value= storeWins)
            displayWins.set(value="Wins: "+str(wins.get()))
            storePayment = intBet * 11
            storingPayment.set(value=storePayment)
            displayPayment.set(value="Payment: +$"+str(storingPayment.get()))
            
        else:
            payment = intBalance
            balance.set(value=str(payment))
            displayBalance.set(value="$"+ str(balance.get()))
            gameStatus.set(value="Draw")
            displayGameStatus.set(value="Game Status: "+str(gameStatus.get()))
            messagebox.showinfo("Draw", "Tied Game!")
            storeDraws = int(draws.get()) + 1
            draws.set(value= storeDraws)
            displayDraws.set(value="Draws: " +str(draws.get()))
            storePayment = 0
            storingPayment.set(value=storePayment)
            displayPayment.set(value="Payment: $"+str(storingPayment.get()))

    if storeHandType == "Consecutive":
        gameStatus.set(value="Draw")
        displayGameStatus.set(value="Game Status: "+str(gameStatus.get()))
        payment = intBalance
        validAddBet.set(value="False")
        balance.set(value=str(payment))
        displayBalance.set(value="$"+ str(balance.get()))
        messagebox.showinfo("Draw", "Tied Game!")       
        storeDraws = int(draws.get()) + 1
        draws.set(value= storeDraws)
        displayDraws.set(value="Draws: " +str(draws.get()))
        storePayment = 0
        storingPayment.set(value=storePayment)
        displayPayment.set(value="Payment: $"+str(storingPayment.get()))

    if storeHandType == "Non-Consecutive":
        if intBalance >0:
            messagebox.showinfo("Notice", "You may make an additional bet or pass bet!")

        displayCard3.set(value=strCard3)
        displaySuitCard3.set(value=storeSuitCard3)

#=========================================================
#Author: Eric Zhou :)
#Purpose: Resets game, additional features, etc
#Date: Oct 29, 2017
#Inputs: Click
#Outputs: Resets display labels
#=========================================================    
        
def userClickedResetGame():
    handType.set(value="")
    between.set(value="")
    payout.set(value="")
    card1.set(value="")
    card2.set(value="")
    card3.set(value="")
    suitCard1.set(value="?")
    suitCard2.set(value="?")
    suitCard3.set(value="?")
    bet.set(value="")
    additionalBet.set(value="")
    firstBet.set(value="False")
    validFirstBet.set(value="False")
    validAddBet.set(value="True")
    handType.set(value="")
    displayHandType.set(value="Hand Type: " + str(handType.get()))
    gameStatus.set(value="")
    displayGameStatus.set(value="Game Status: "+str(gameStatus.get()))
    storingPayment.set(value="")
    displayPayment.set(value="Payment: $"+str(storingPayment.get()))
    
    if int(balance.get()) == 0:
        messagebox.showinfo("No Money!", "You lost all your money! Gambling is bad!")
        balance.set(value="100")
        displayBalance.set(value="$"+ str(balance.get()))
        wins.set(value="0")
        loss.set(value="0")
        draws.set(value="0")
        totalBet.set(value="0")
        gameStatus.set(value="")
        displayGameStatus.set(value="Game Status: "+str(gameStatus.get()))
        displayWins.set(value="Wins: " + str(wins.get()))
        displayLoss.set(value="Loss: " + str(loss.get()))
        displayDraws.set(value="Draws: " + str(draws.get()))

            
#MAIN WINDOW
mainWindow = Tk()
mainWindow.title("Red Dog")

#Menu
menubar = Menu(mainWindow)

#File Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open Saved Game",
                     command=lambda:messagebox.showerror("Error", "No saved game found!"))
filemenu.add_command(label="Save Game",
                     command=lambda:messagebox.showerror("Error", "This feature is not added in yet!"))
filemenu.add_separator()
filemenu.add_command(label="Exit Game",
                     command=lambda:(messagebox.showinfo("Bye!", "Good Bye Player!"),mainWindow.destroy()))
menubar.add_cascade(label="File", menu=filemenu)

#Edit Menu
editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label="Undo Bet",
                     command=lambda:messagebox.showerror("Error", "You cannot undo a bet!"))
editmenu.add_command(label="Redo Bet",
                     command=lambda:messagebox.showerror("Error", "This feature is not added yet!"))
editmenu.add_command(label="Redo Life",
                     command=lambda:messagebox.showerror("Error", "You cannot redo life! Do not gamble!"))
menubar.add_cascade(label="Edit", menu=editmenu)

#Help Menu
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="About",
                     command=lambda:messagebox.showinfo(" About ", " This program was created by Eric Zhou :) "))
menubar.add_cascade(label="Help", menu=helpmenu)

#Main Window Config
mainWindow.config(menu=menubar, bg="maroon", width= 450, height = 600)

#StringVars

#Betting
firstBet = StringVar()
validFirstBet = StringVar()
validFirstBet.set(value="False")
balance = StringVar()
balance.set(value="100")
displayBalance = StringVar()
displayBalance.set(value="$"+ str(balance.get()))
bet = StringVar()
additionalBet = StringVar()
validAddBet = StringVar()
validAddBet.set(value="True")
storingPayment = StringVar()
storingPayment.set(value="")
displayPayment = StringVar()
displayPayment.set(value="Payment: $"+str(storingPayment.get()))

#Cards (♥♠♣♦)
handType = StringVar()
displayHandType = StringVar()
displayHandType.set(value="Hand Type: " + str(handType.get()))
between = StringVar()
payout = StringVar()
card1 = StringVar()
card1.set(value="")
card2 = StringVar()
card2.set(value="")
card3 = StringVar()
card3.set(value="")
suitCard1 = StringVar()
suitCard1.set(value="?")
suitCard2 = StringVar()
suitCard2.set(value="?")
suitCard3 = StringVar()
suitCard3.set(value="?")
displayCard3 = StringVar()
displaySuitCard3 = StringVar()

#Scoreboard
message = StringVar()
message.set(value="")
wins = StringVar()
wins.set(value="0")
loss = StringVar()
loss.set(value="0")
draws = StringVar()
draws.set(value="0")
totalBet = StringVar()
totalBet.set(value="0")
gameStatus = StringVar()
gameStatus.set(value="")
displayGameStatus = StringVar()
displayGameStatus.set(value="Game Status: "+str(gameStatus.get()))
displayWins = StringVar()
displayWins.set(value="Wins: " + str(wins.get()))
displayLoss = StringVar()
displayLoss.set(value="Loss: " + str(loss.get()))
displayDraws = StringVar()
displayDraws.set(value="Draws: " + str(draws.get()))


#GUIs, width= 750, height = 350
Label(mainWindow, text=("Red Dog"), bg="maroon", fg="white", font=("Arial, bold", 18)).place(x=175, y=3)


#Frame
Frame(mainWindow, width = 400, height = 315, highlightthickness=4, highlightbackground="black", bg="firebrick4").place(x=25, y=255)

#BELOW
Label(mainWindow, textvariable=displayHandType,fg ="white", bg="firebrick4", font=("Arial", 14)).place(x=100, y=375)
Label(mainWindow, textvariable=displayGameStatus,fg ="white", bg="firebrick4", font=("Arial", 14)).place(x=100, y=405)
Label(mainWindow, textvariable=displayWins,fg ="white", bg="firebrick4", font=("Arial", 14)).place(x=100, y=435)
Label(mainWindow, textvariable=displayLoss,fg ="white", bg="firebrick4", font=("Arial", 14)).place(x=100, y=465)
Label(mainWindow, textvariable=displayDraws,fg ="white", bg="firebrick4", font=("Arial", 14)).place(x=100, y=495)
Label(mainWindow, textvariable=displayPayment,fg ="white", bg="firebrick4", font=("Arial", 14)).place(x=100, y=525)


#Balance, Bet, Additional Bet, Pass Bet, Reset Game
Label(mainWindow, text="Balance:", bg="firebrick4", fg="white", font=("Arial", 14)).place(x=34, y=265)
Label(mainWindow, textvariable=displayBalance, bg="firebrick4", fg="white", font=("Arial", 14)).place(x=110, y=265)
Label(mainWindow, text="Enter Bet: $", bg="firebrick4", fg="white", font=("Arial", 12)).place(x=34, y=300)
Entry(mainWindow, textvariable=bet, width=7, font=("Arial",12)).place(x=123, y=300)
Button(mainWindow, text="BET!", width=16, bg="white", fg="black", font=("Arial",12), command=lambda:userClickedBet()).place(x=37,y=335)
Button(mainWindow, text="ADDITIONAL BET!",width=16, bg="white", fg="black", font=("Arial",12), command=lambda:userClickedAddBet()).place(x=233,y=265)
Button(mainWindow, text="PASS BET!",width=16, bg="white", fg="black", font=("Arial",12), command=lambda:userClickedPass()).place(x=233,y=300)
Button(mainWindow, text="RESET GAME!",width=16, bg="white", fg="black", font=("Arial",12), command=lambda:userClickedResetGame()).place(x=233,y=335)


#Frame for Cards
Frame(mainWindow, bd = 3, highlightthickness=4, highlightbackground="black", bg="firebrick4", height=210, width=400).place(x=25, y=35)


#Card1
Frame(mainWindow, highlightthickness=4, highlightbackground="black",bg="white", width =100, height=150).place(x=45, y=50)
Label(mainWindow, text = "First Card", fg ="white",bg="firebrick4", font=("Arial", 12)).place(x=55, y=208)
Label(mainWindow, textvariable=suitCard1, fg ="black",bg="white", font=("Arial", 52)).place(x=71, y=85)
Label(mainWindow, textvariable=card1, fg="black", bg='white', font=("Arial", 18)).place(x=49, y=54)

#Card2
Frame(mainWindow, highlightthickness=4, highlightbackground="black",bg="white", width =100, height=150).place(x=171, y=50)
Label(mainWindow, text = "Second Card", fg ="white",bg="firebrick4", font=("Arial", 12)).place(x=175, y=208)
Label(mainWindow, textvariable=suitCard2, fg ="black",bg="white", font=("Arial", 52)).place(x=194, y=85)
Label(mainWindow, textvariable=card2, fg="black", bg='white', font=("Arial", 18)).place(x=178, y=54)

#Card3
Frame(mainWindow, highlightthickness=4, highlightbackground="black",bg="white", width =100, height=150).place(x=302, y=50)
Label(mainWindow, text = "Third Card", fg ="white",bg="firebrick4", font=("Arial", 12)).place(x=313, y=208)
Label(mainWindow, textvariable=suitCard3, fg ="black",bg="white", font=("Arial", 52)).place(x=328, y=85)
Label(mainWindow, textvariable=card3, fg="black", bg='white', font=("Arial", 18)).place(x=307, y=54)


mainloop()







