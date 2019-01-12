#Date: Sept 22, 2017
#Author: Eric Zhou
#Purpose: Give customers back their change
#Inputs: keyboard
#Output: Screen/Console
#=================================

purchase = -1
cash = -1

while purchase <0:
    purchase = float(input("Enter the amount of the purchase!: "))
    
while cash < 0 or cash < purchase:
    cash = float(input("Enter the amount you paid!: "))

print("Purchase Price", purchase)

print("Cash Given", cash)

change = cash - purchase
print("Change due:", round(change,2))
    
bill20 = change // 20
if bill20 >0:
    change = change - bill20*20
    print(bill20, '-', '$20.00 =', bill20*20)
    
bill10 = change // 10
if bill10 >0:
    change = change - bill10*10
    print(bill10, '-', '$10.00 =', bill10*10)
    
bill5 = change // 5
if bill5 >0:
    change = change - bill5*5
    print(bill5, '-', '$5.00 =', bill5*5)
    
toonie = change // 2
if toonie >0:
    change = change - toonie*2
    print(toonie, '-', '$2.00 =', toonie*2)
    
loonie = change // 1
if loonie >0:
    change = change - loonie*1
    print(loonie, '-', '$1.00 =', loonie *1)
    
quarter = change // 0.25
if quarter >0:
    change = change - quarter*0.25
    print(quarter, '-', '$0.25 =', quarter*0.25)
    
dime = change // 0.1
if dime >0:
    change = change - dime*0.10
    print(dime, '-', '$0.10 =', dime*0.1)
    
nickel = change // 0.05
if nickel >0:
    change = change - nickel*0.05
    print(nickel, '-', '$0.05=', nickel *0.05)

