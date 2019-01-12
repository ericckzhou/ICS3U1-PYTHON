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
#Input: Self, Month, day, year
#Output: No output
#Methods =================================================
#__str__:                - Returns the date in string-word form. eg Friday, July 1 2017.
#returnMonthName:        - Returns the month name of a entered number for month.
#returnLeapYear:         - Returns True or False if the entered date is a leap year or not.
#returnMaxDay:           - Returns the max day of the entered month.
#calcZeller:             - Calculates the weekday of the date entered.
#returnFirstDayOfMonth:  - Returns the first day / start of the weekday of the entered date.
#returnDayName:          - Returns the weekday name.
#displayCalendar:        - Displays the calendar of a entered date.
#dayOfYear:              - Returns the number of days in a year of the entered date.
#calcValid:              - Sees if the date entered is valid.
#getDate:                - Asks user input for date.
#__gt__:                 - Determines if date1 is greater than date2 entered
#__lt__:                 - Determines if date1 is less than date2 entered
#__gtet__:               - Determines if date1 is greater than equal to date2 entered
#__ltet__:               - Determines if date1 is less than equal to date2 entered
#__eq__:                 - Determines if date1 equals to date2 entered
#__ne__:                 - Determines if date1 does not equal to date2 entered
#__sub__:                - Subtracts date1 and date2 to find the difference of days between them.
#__add__:                - Adds date1 and date2 and returns the new date from the sum of the two dates.
#=========================================================

class Date():
    def __init__(self, month=1, day=1, year=2000):
        #The month of the date
        self.month = month
        #The day of the date
        self.day = day
        #The year of the date
        self.year = year

#===============================================================
#Author: Eric Zhou
#Date: 11/7/2017
#Purpose: Gets the date in name/word form
#Input: self
#Output: Returns str date
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
        monthName = ""
        
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

        #Header
        print("")
        print("%27s" % date)
        print("%17s" % self.returnMonthName(), self.year)
        print("")
        print("Sun", end = "")
        print("%5s" % "Mon", end = "")
        print("%5s" % "Tue", end = "")
        print("%5s" % "Wed", end = "")
        print("%5s" % "Thu", end = "")
        print("%5s" % "Fri", end = "")
        print("%5s" % "Sat")

        #Printing days
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

        if leapYear == True:
            totalDays += 1

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
        validMonth = False
        setDate = False
        
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
            else:
                print("Your last year input is not valid")

        if validMonth == True and validDay == True and validYear == True:
            setDate = True
            self.day = int(day)
            self.month = int(month)
            self.year = int(year)

        return setDate
    
#===============================================================
#Author: Eric Zhou
#Date: 12/8/2017
#Purpose: Sees if date1 is greater than date2
#Input: self, date2
#Output: return boolean
#===============================================================
    def __gt__(self, date2):
        greaterThan = True
        if self.year > date2.year:
            greaterThan = True
        if date2.year > self.year:
            greaterThan = False
        if self.year == date2.year:
            if self.month > date2.month:
                greaterThan = True
            if date2.month > self.month:
                greaterThan = False
            if self.month == date2.month:
                if self.day > date2.day:
                    greaterThan = True
                if date2.day > self.day:
                    greaterThan = False
                    
        return greaterThan
    
#===============================================================
#Author: Eric Zhou
#Date: 12/8/2017
#Purpose: Sees if date1 is less than date2
#Input: self, date2
#Output: Returns boolean
#===============================================================
    def __lt__(self, date2):
        lessThan = True
        if self.year < date2.year:
            lessThan = True
        if date2.year < self.year:
            lessThan = False
        if self.year == date2.year:
            if self.month < date2.month:
                lessThan = True
            if date2.month < self.month:
                lessThan = False
            if self.month == date2.month:
                if self.day < date2.day:
                    lessThan = True
                if date2.day < self.day:
                    lessThan = False

        return lessThan
#===============================================================
#Author: Eric Zhou
#Date: 12/8/2017
#Purpose: Sees if date1 is greater than equal to date2
#Input: self, date2
#Output: Returns boolean
#===============================================================
    def __gtet__(self, date2):
        greaterThan = True
        if self.year >= date2.year:
            greaterThan = True
        if date2.year >= self.year:
            greaterThan = False
        if self.year == date2.year:
            if self.month >= date2.month:
                greaterThan = True
            if date2.month >= self.month:
                greaterThan = False
            if self.month == date2.month:
                if self.day >= date2.day:
                    greaterThan = True
                if date2.day >= self.day:
                    greaterThan = False
                    
        return greaterThan
#===============================================================
#Author: Eric Zhou
#Date: 12/8/2017
#Purpose: Sees if date1 is less than equal to date2
#Input: self, date2
#Output: Returns boolean
#===============================================================
    def __ltet__(self, date2):
        lessThan = True
        if self.year <= date2.year:
            lessThan = True
        if date2.year <= self.year:
            lessThan = False
        if self.year == date2.year:
            if self.month <= date2.month:
                lessThan = True
            if date2.month <= self.month:
                lessThan = False
            if self.month == date2.month:
                if self.day <= date2.day:
                    lessThan = True
                if date2.day <= self.day:
                    lessThan = False

        return lessThan
#===============================================================
#Author: Eric Zhou
#Date: 12/8/2017
#Purpose: Sees if date1 is equal to date2
#Input: self, date2
#Output: Returns boolean
#===============================================================
    def __eq__(self, date2):
        if self.month == date2.month and self.day == date2.day and self.year == date2.year:
            equal = True
        else:
            equal = False

        return equal

#===============================================================
#Author: Eric Zhou
#Date: 12/8/2017
#Purpose: Sees if date1 is not equal to date2
#Input: self, date2
#Output: Returns boolean
#===============================================================
    def __ne__(self, date2):
        if not (self.month == date2.month and self.day == date2.day and self.year == date2.year):
            notEqual = True
        else:
            notEqual = False

        return notEqual
    
#==================================================
#Author: Eric Zhou
#Date: 12/9/2017
#Purpose: Gets the difference of days in two dates
#Input: self, date2
#Output: differenece of the two dates
#==================================================
    def subtractDate(self, date2):
        useYear1 = self.year
        useYear2 = date2.year
        useMonth1 = self.month
        useMonth2 = date2.month
        useDay1 = self.day
        useDay2 = date2.day

        totalDays = 0
        #Getting the totalDays when date1 == date2
        #(date1.month == date2.month, date1.day == date2.day, date1.year == date2.year)
        if self.year > date2.year:
            while self.year != date2.year:
                if self.returnLeapYear() == True:
                    totalDays += 366
                else:
                    totalDays += 365
                self.year -= 1
                
        if date2.year > self.year:
            while date2.year != self.year:
                if date2.returnLeapYear() == True:
                    totalDays += 366
                else:
                    totalDays += 365
                date2.year -= 1

        if self.month > date2.month:
            totalMonths = self.month
            while self.month != date2.month:
                self.month -= 1
                totalDays += self.returnMaxDay()


        if date2.month > self.month:
            totalMonths = date2.month
            while self.month != date2.month:
                date2.month -= 1
                totalDays += date2.returnMaxDay()


        if self.day > date2.day:
            while self.day != self.day:
                totalDays += 1
                self.day -= 1

        if date2.day > self.day:
            while self.day != date2.day:
                totalDays += 1
                date2.day -= 1
                
        self.year = useYear1
        date2.year = useYear2
        self.month = useMonth1
        date2.month = useMonth2
        self.day = useDay1
        date2.day = useDay2
        
        return totalDays
#==================================================
#Author: Eric Zhou
#Date: 12/10/2017
#Purpose: Adds the two date together to produce a new date
#Input: self, date2
#Output: new date
#==================================================
    def addDate(self, date2):
        #Making date1.year == date2.year
        if self.year > date2.year:
            while self.year != date2.year:
                if self.returnLeapYear() == True:
                    self.day += 366
                else:
                    self.day += 365
                self.year -= 1

        if date2.year > self.year:
            while date2.year != self.year:
                if date2.returnLeapYear() == True:
                    date2.day += 366
                else:
                    date2.day += 365
                date2.year -= 1

        #Setting the new date's year
        if self.year == date2.year:
            newYear = self.year

        day1 = self.dayOfYear()
        day2 = date2.dayOfYear()

        #Sets the greatest new date's month between date1's month and date2's month
        if self.month > date2.month:
            newMonth = self.month
        else:
            newMonth = date2.month

        #Cannot have a month greater than 12
        while newMonth > 12:
            newYear += 1
            newMonth -= 12

        #Finding the difference in days between 2 dates
        if day1 > day2:
            diffDay = self.day + (day1 - day2)
        else:
            diffDay = date2.day + (day2 - day1)

        #Setting new date's day
        newDay = diffDay
        #Creating a third date
        newDate = Date(newMonth, newDay, newYear)

        #Validating days
        maxDay = newDate.returnMaxDay()
        while newDate.day > maxDay:
            newDate.day -= maxDay
            newDate.month += 1
            maxDay = newDate.returnMaxDay()

            #Validating month
            if newDate.month > 12:
                newDate.month -= 12
                newDate.year += 1
                
        return newDate
        

#-------------- MAIN CODE -------------------------------------------#
redo = True
while redo == True:
    firstDate = Date()
    secondDate = Date()
    date1 = firstDate.getDate()
    date2 = secondDate.getDate()

    greaterThan = firstDate.__gt__(secondDate)
    if greaterThan == True:
        firstDate, secondDate = secondDate, firstDate
    
    totalDays1 = firstDate.dayOfYear()
    totalDays2 = secondDate.dayOfYear()
    
    validDate = False
    checkDate1 = firstDate.calcValid()
    checkDate2 = secondDate.calcValid()
    
    
    if checkDate1 == True and checkDate2 == True:
        differenceDay = firstDate.subtractDate(secondDate)
        newDate = firstDate.addDate(secondDate)
        myDate = Date(newDate.month, newDate.day, newDate.year)
        strDate = myDate.__str__()
        myCalender = myDate.displayCalendar()
        numberOfDays = myDate.dayOfYear()

        print("The two dates entered were added and created " + str(myDate))
        print("NOTICE: The date shown above has a total of " + str(numberOfDays) + " days! ")
        print("NOTICE: The difference in the two date entered is " + str(differenceDay) + " days! ")
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
#---------------------------------------------------------------------#



            
