#=============================================
#Author: Eric Zhou
#Date: 11/6/2017
#Purpose: To create a date class
#Input: Keyboard
#Output: Date
#=============================================

from tkinter import *

#=========================================================
#Author: Eric Zhou
#Date: 11/6/2017
#Purpose: a date class which holds components of the date
#Input: self, month, day, year
#Output: No output
#=========================================================

class Date():
    def __init__(self, month=1, day=1, year=2000):
        self.month = month
        self.day = day
        self.year = year

#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Gets the date in name/word form
#Input: self
#Output: Returns date
#===============================================================

    def __str__(self):
        dayNumber = self.calcZeller()
        dayName = self.returnDayName()
        monthName = self.returnMonthName()
        year = str(self.year)
        day = str(self.day)
        return (dayName + ', ' + day + ' ' + monthName + ' ' + year)
    
#=========================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Returns the month in the name
#Input: self
#Output: Month Name
#=========================================================
        
    def returnMonthName(self):
        
        if self.month == 1:
            monthName = "January"
        elif self.month == 2:
            monthName = "February" 
        elif self.month == 3:
            monthName = "March"
        elif self.month == 4:
            monthName = "April" 
        elif self.month == 5:
            monthName = "May"
        elif self.month == 6:
            monthName = "June"
        elif self.month == 7:
            monthName = "July"
        elif self.month == 8:
            monthName = "August"
        elif self.month == 9:
            monthName = "September"
        elif self.month == 10:
            monthName = "October"
        elif self.month == 11:
            monthName = "November"
        elif self.month == 12:
            monthName = "December"

        return monthName

#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Sees if leap year is true or not with a given date
#Input: self
#Output: Returns leap year == True or False
#===============================================================

    def returnLeapYear(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            leapYear = True
        else:
            leapYear = False
            
        return leapYear

#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Sees the max day of a given month
#Input: self
#Output: Returns the max day of that month
#===============================================================

    def returnMaxDay(self):
        month = self.month
        leapYear = self.returnLeapYear()
        
        if month == 9 or month == 6 or month == 4 or month == 11:
            maxDay = 30
        elif month == 2 and leapYear == True:
            maxDay = 29
        elif month == 2 and leapYear == False:
            maxDay = 28
        else:
            maxDay = 31
            
        return maxDay

#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Sees what the weekday of a given date is
#Input: self
#Output: Returns the weekday of a given date
#===============================================================

    def calcZeller(self):
        month = int(self.month)
        year = int(self.year)
        day = int(self.day)
        
        m = month - 2
        y = year
        if m <=0:
            m += 12
            y -= 1
        p = y // 100
        r = y % 100

        return (day + (26*m -2) //10 + r + r // 4 + p // 4 + 5 * p) % 7

#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Returns the First Day of that Month given
#Input: self
#Output: Returns the weekday of that month's first day
#===============================================================

    def returnFirstDayMonth(self):
        month = int(self.month)
        year = int(self.year)
        day = 1
        
        m = month - 2
        y = year
        if m <=0:
            m += 12
            y -= 1
        p = y // 100
        r = y % 100

        return (day + (26*m -2) //10 + r + r // 4 + p // 4 + 5 * p) % 7

#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Sees the day name of the given date
#Input: self
#Output: Returns the day name of the given date
#===============================================================

    def returnDayName(self):
        day = self.calcZeller()
        if day == 0:
            dayName = "Sunday"
        elif day == 1:
            dayName = "Monday"
        elif day == 2:
            dayName = "Tuesday"
        elif day == 3:
            dayName = "Wednesday"
        elif day == 4:
            dayName = "Thursday"
        elif day == 5:
            dayName = "Friday"
        elif day == 6:
            dayName = "Saturday"
        
        return dayName

#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Display a calender of a date given
#Input: self
#Output: Returns calendar of the given date
#===============================================================

    def displayCalendar(self):
        date = self.__str__()
        countDays = 1
        useDay = self.day
        self.day = 1

        print("")
        print("%27s" % date)
        print("")
        print("Sun", end = "")
        print("%5s" % "Mon", end = "")
        print("%5s" % "Tue", end = "")
        print("%5s" % "Wed", end = "")
        print("%5s" % "Thu", end = "")
        print("%5s" % "Fri", end = "")
        print("%5s" % "Sat")

        for count in range(self.calcZeller()):
            print("%5s" % "", end = "")
        for count in range(5 - self.calcZeller() + 1):
            print(str(countDays) + "%4s" % "", end = "")
            countDays += 1
        print(str(countDays))
        countDays += 1
        while (countDays < self.returnMaxDay()):
            for count in range(6):
                if (countDays < self.returnMaxDay()):
                    if (countDays < 10):
                        print(str(countDays) + "%4s" % "", end = "")
                        countDays += 1
                    else:
                        print(str(countDays) + "%3s" % "", end = "")
                        countDays += 1
            print(str(countDays))
            countDays += 1
            
        while (countDays <= self.returnMaxDay()):
            print(str(countDays) + "%3s" % "")
            countDays += 1

        print("")

        self.day = useDay        
#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Finds the # of days in the year of a given date
#Input: self
#Output: Returns the # of days in the year
#===============================================================
                
    def dayOfYear(self):
        day = self.day
        month = self.month
        year = self.year
        leapYear = self.returnLeapYear()
        sMonth = self.month
        
        totalMonth = 1
        totalDays = 0
        while (totalMonth != (month)):
            self.month = totalMonth
            maxDay = self.returnMaxDay()
            totalDays += maxDay
            totalMonth += 1

        if totalMonth == month:
            totalDays += day
            self.month += 1

        return totalDays

#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Sees if the date given is valid
#Input: self
#Output: Returns valid is True or False
#===============================================================

    def calcValid(self):
        valid = True
        month = self.month
        day = self.day
        year = self.year

            
        intMonth = int(month)   
        if not intMonth in range(1,13):
            print("Your last month input was not in the range 1 - 12")
            valid = False

        if valid == True:
            leapYear = self.returnLeapYear()
            maxDay = self.returnMaxDay()
            intDay = int(day)

            if month ==2 and (intDay not in range(1, maxDay+2)) and leapYear == True:
                print("Your last day input was not in the range 1 - " + str(maxDay+1))
                valid = False
            
            if (intDay not in range(1, maxDay+1)) and leapYear == False:
                print("Your last day input was not in the range 1 - " + str(maxDay))
                valid = False

            if not (year in range(1600, 10000)):
                valid = False
                print("Your last year input was not in range year 1600-9999")
                
        return valid

#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Gets date
#Input: self
#Output: Returns date object
#===============================================================

    def getDate(self):
        Date = False
        validMonth = False
        while validMonth == False:
            month = input("Enter the month (Numeric only): ")
            if month.isdigit():
                validMonth = True
            else:
                print("Your last input was not a valid positive integer")
                

        validDay = False
        while validDay == False:
            day = input("Enter the day (Numeric only): ")
            if day.isdigit():
                validDay = True      
            else:
                print("Your last input was not a valid positive integer")
        validYear = False
        while validYear == False:
            year = input("Enter the year (Numeric only): ")
            if year.isdigit():
                validYear = True
        
        if validDay == True and validMonth == True and validYear == True:
           
           Date = True
           self.day = int(day)
           self.month = int(month)
           self.year = int(year)

        return Date
        

#-------------- MAIN CODE -------------------------------------------
redo = True
while redo == True:
    myDate = Date()
    myDate.getDate()
    checkDate = myDate.calcValid()
    if checkDate == True:
        strDate = myDate.__str__()
        myCalender = myDate.displayCalendar()
        numberOfDays = myDate.dayOfYear()
        print("The total days of the day entered is " + str(numberOfDays) + " days!")
        print("")
        print("Enter anything if you want to run the program!")
        tryAgain = input("Type 'N' if you do not want to rerun the program : ")
        if tryAgain == "n" or tryAgain == "N":
            redo = False
    else:
        print("Invalid Date! Retry again!")
        tryAgain = input("Would you like to try again? Y/N : ")
        if tryAgain == "n" or tryAgain == "N":
            redo = False


#---------------------------------------------------------------------



            
