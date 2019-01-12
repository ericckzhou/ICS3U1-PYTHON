#============================================
#Author: Eric Zhou :) 
#Date: Oct 18, 2017
#Purpose: To create a game of Red Dog
#Inputs: Keyboard, bet amounts
#Outputs: Console/Screen, balance, hand
#============================================
import random
import math

#The Game Title
print("")
print(" ============================== ")
print(' WELCOME TO THE GAME "RED DOG"')
print("    Created by: Eric Zhou ")
print(" ============================== ")
print("")

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
        strCard = "(Two "
    if card == 3:
        strCard = "(Three "
    if card == 4:
        strCard = "(Four "
    if card == 5:
        strCard = "(Five "
    if card == 6:
        strCard = "(Six "
    if card == 7:
        strCard = "(Seven "
    if card == 8:
        strCard = "(Eight "
    if card == 9:
        strCard = "(Nine "
    if card == 10:
        strCard = "(Ten "
    if card == 11:
        strCard = "(Jack "
    if card == 12:
        strCard = "(Queen "
    if card == 13:
        strCard = "(King "
    if card == 14:
        strCard = "(Ace "
    return strCard

#==================================================================
#Author: Eric Zhou :) 
#Purpose: Giving the word number of that card type
#Date: Oct 18, 2017
#Inputs: Word of the number of the card, keyboard
#Outputs: Returns the word of the number of the card plus the suit
#==================================================================
def getCardSuit(strCard):
    cardSuit = random.randint(1,4)
    if cardSuit == 1:
        strCard += "of ♠)"
        
    if cardSuit == 2:
        strCard += "of ♥)"
        
    if cardSuit == 3:
        strCard += "of ♣)"
        
    if cardSuit == 4:
        strCard += "of ♦)"
        
    cardSuit = 0
    return strCard

#==============================================================================
#Author: Eric Zhou :)
#Purpose: Converts TwoCards Object to integer and Prints the hand of the player 
#Date: Oct 18, 2017
#Inputs: hand, keyboard
#Output: player's hand
#==============================================================================
def printHand(hand):
    intCard1 = hand.card1
    intCard2 = hand.card2
    return print("Integer Hand: " + str(intCard1) + ' , ' + str(intCard2))

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
    if card3 in range(card1 +1, card2 -1) or card3 in range(card2 +1, card1 -1):
        between = True
    else:
        between = False
    return between

#=================================================
#Author: Eric Zhou :)
#Purpose: Getting positive and valid bet from user
#Date: Oct 18, 2017
#Inputs: balance and bet of the user, keyboard
#Outputs: integer of user bet
#=================================================
def getPositiveBet(balance, bet):
    balance = balance
    low = balance - balance
    high = balance
    intUserBet = low -1
    while (intUserBet < low or intUserBet > high):
        strUserBet = ""
        while (not strUserBet.isdigit()):
            if bet >0 and balance > bet:
                strUserBet = input("Enter bet: " + '$' + str(1) + ' - ' + '$' + str(bet) + ': ')
            else:
                strUserBet = input("Enter bet: " + '$' + str(1) + ' - ' + '$' + str(balance) + ': ')
                
            if (not strUserBet.isdigit()):
                print("Game: Player's last input was not a valid positive value; please try again.  ")
        intUserBet = int(strUserBet)
        if (intUserBet < low or intUserBet > bet and bet != 0):
            print("Game: Player's last input was not in " + '$' + str(1) + ' - ' + '$' + str(bet) + '! ')
        if (intUserBet < low or intUserBet > high ):
            print("Game: Player's last input was not in " + '$' + str(1) + ' - ' + '$' + str(balance) + '! ')     
    return intUserBet

#================================================
#Author: Eric Zhou :)
#Purpose: Runs the game Red Dog
#Date: Oct 18, 2017
#Inputs: Balance and playCount of User, keyboard
#Outputs: Balance
#================================================
#Main Code
def game(balance, playCount):
    balance = balance
    print("Balance: $" + str(balance))
    bet = getPositiveBet(balance, 0)
    while bet <= 0:
        print("Your bet has to be greater than 0! ")
        bet = getPositiveBet(balance, 0)

    #I will add back bet if player wins
    balance -= bet    
    print("")
    hand = getHand()
    printHand(hand)
    
    intCard1 = hand.card1
    intCard2 = hand.card2
    strCard1 = getStrCard(intCard1)
    strCard2 = getStrCard(intCard2)
    suitCard1 = getCardSuit(strCard1)
    suitCard2 = getCardSuit(strCard2)
    
    #Avoiding same cards with same suits
    while suitCard1 == suitCard2:
        suitCard1 = getCardSuit(strCard1)
        
    print("Suit Hand: " + str(suitCard1) + str(suitCard2))
    intCard3 = getCard()
    strCard3 = getStrCard(intCard3)
    suitCard3 = getCardSuit(strCard3)
    
    #Avoiding same cards with same suits
    while suitCard3 == suitCard1 or suitCard3 == suitCard2:
        suitCard3 = getCardSuit(strCard3)
    
    handType = getHandType(hand)
    print("Game: Player has " + str(handType) + " hand. ")
    print("")
    spread = getSpread(hand)
    payout = getPayout(spread)
    between = ifBetween(hand, intCard3)

    if handType == 'Pair':
        print("Game: Player drew " + str(suitCard3) + '! ')
        if intCard3 == intCard1 and intCard3 == intCard2:
            payment = bet * 11
            #Added bet
            balance += payment + bet
            print("Game: Congratulations Player, you won $" + str(payment) +'! ')
            print("Balance: $" + str(balance))
        else:
            print("Game: Tied Game! ")
            print("")
            #Added bet
            balance += bet
            print("Balance: $" + str(balance))
            
    if handType == "Consecutive":
        print("Game: Tied Game! ")
        #Added bet
        balance += bet
        print("")
        print("Balance: $" + str(balance))

    if handType == "Non-Consecutive":
        additionalBet = 0
        if not balance == 0:
            anotherBet = input("Would Player like to make an additional bet? : Y/N ")
            while not (anotherBet == 'Y' or anotherBet == 'y' or anotherBet == 'N' or anotherBet == 'n'):
                 print("ATTENTION: Player's last input was not Y or N! ")
                 anotherBet = input("Would Player like to make an additional bet? : Y/N ")
            if anotherBet == 'Y' or anotherBet == 'y':
                additionalBet = getPositiveBet(balance, bet)
                if additionalBet == 0 and balance != 0:
                    print("Game: Player's last bet was not in the betting range! ")
                    additionalBet = getPositiveBet(balance, bet)
                while additionalBet > bet:
                    print("Game: Player's last bet was greater than the original! ")
                    additionalBet = getPositiveBet(balance, bet)
            if anotherBet == 'N' or anotherBet == 'n':
                additionalBet = 0

        #I will add back the additionalBet if the player wins
        balance -= additionalBet 
        print("")
        print("Game: Player drew " + str(suitCard3) + '! ')
        
        if between == True:
            payment = (bet + additionalBet) * payout
            #Added bets
            balance += payment + bet + additionalBet
            print("Game: Congratulations Player, you won $" + str(payment) + "!")
            print("")
            print("Balance: $" + str(balance))
            
        if between == False:
            print("Game: Player lost! ")
            print("")
            print("Balance: $" + str(balance))
            
    return balance

#Start Of Red Dog            
balance = game(100, 0)
playCount = 0
#Rerunning Red Dog
replay = True
while replay == True:
    
    play = input("Would Player like to play again? Y/N ")
    while not (play == "Y" or play == "y" or play == 'N' or play == 'n'):
        print("Your last input was not Y or N! ")
        play = input("Would Player like to play again? Y/N ")
        
    if play == "Y" or play == "y":
        playCount += 1
        if balance != 0:
            print(" ")
            print(" ================================= ")
            print("   - - - Reloading Red Dog - - -   ")
            print("            . . . . .              ")
            print(" ================================= ")
            print(" ")
        
        if balance == 0:
            print("Game: Player lost all your money! Never gamble! ")
            replay = False
        else:
            balance = game(balance, playCount)
            
    if play == 'N' or play == 'n':
        replay = False
        print("Game: Never Gamble, it's bad! ")

        
            

