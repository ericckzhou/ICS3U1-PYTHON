#Author: Eric Zhou
#Date: Oct 4, 2017
#Purpose: To produce a table of mortgage payment rates monthly per years
#Input: Keyboard
#Outputs: Screen/Console
#========================================================================


mortgageAmount = -1
customRate = ""
rate = 0

while mortgageAmount <= 0:
    mortgageAmount = int(input("Enter your mortgage amount: "))
    if mortgageAmount <= 0:
        print("Please enter a valid mortgage amount.")

# Asking for Custom Rates

while not ((customRate == "Y" or customRate == "y") or (customRate == "N" or customRate == "n")):
    customRate = input("Do you want a custom rate? (Y/N): ")
    if (customRate == "Y" or customRate == "y"):
        rate1 = -1
        rate2 = -1
        while not (rate1 > 0 and rate2 > 0 and rate2 > rate1):
            rate1 = int(input("Enter the starting rate: "))
            rate2 = int(input("Enter the ending rate: "))

print("Mortage Amount:", mortgageAmount)
print("%68s" % ("Years"))
print("Interest", end = "")

# Printing Years List

years = 5

for years in range(5, 36, 5):
    print("%15s" % years, end = "")

print("")

# Mortgage Calculations/Table

if (customRate == 'Y' or customRate == 'y'):
    for rate in range((rate1*100), (rate2*100+1), 25):
        years = 5
        interestCount = 0
        interest = 0.25
        print("%8s" % ("%0.2f" % (rate/100)), end = "")
        
        for interestCount in range(7):
            months = years * 12
            i = (1 + ((rate/100)/200))**(1/6) -1
            f = 1 / ((1 -(1+i)**-months) /i)
            monthlyPayment = f * mortgageAmount
            print("%15s" % ("$" + "%0.2f" % (monthlyPayment)), end = "")
            years += 5
            
        print("")
        
else:
    for rate in range(25, 601, 25):
        years = 5
        interestCount = 0
        print("%8s" % ("%0.2f" % (rate/100)), end = "")
        
        for interestCount in range(7):
            months = years * 12
            i = (1 + ((rate/100)/200))**(1/6) -1
            f = 1 / ((1 -(1+i)**-months) /i)
            monthlyPayment = f * mortgageAmount
            print("%15s" % ("$" + "%0.2f" % (monthlyPayment)), end = "")
            years += 5
                
        print("")

print("")

#Total Cost of Mortgage Table

print("%72s" % ("Total Cost of Mortgage"))

if (customRate == 'Y' or customRate == 'y'):
    for rate in range((rate1*100), (rate2*100+1), 25):
        years = 5
        interestCount = 0
        print("%8s" % ("%0.2f" % (rate/100)), end = "")
        
        for interestCount in range(7):
            months = years * 12
            i = (1 + ((rate/100)/200))**(1/6) -1
            f = 1 / ((1 -(1+i)**-months) /i)
            monthlyPayment = f * mortgageAmount
            total = (monthlyPayment * months) - mortgageAmount
            print("%15s" % ("$" + "%0.2f" % total), end = "")
            years += 5
            
        print("")
        
else:
    for rate in range(25, 601, 25):
        years = 5
        interestCount = 0
        print("%8s" % ("%0.2f" % (rate/100)), end = "")
        
        for interestCount in range(7):
            months = years * 12
            i = (1 + ((rate/100)/200))**(1/6) -1
            f = 1 / ((1 -(1+i)**-months) /i)
            monthlyPayment = f * mortgageAmount
            total = (monthlyPayment * months) - mortgageAmount
            print("%15s" % ("$" + "%0.2f" % (total)), end = "")
            years += 5
            
        print("")
    


