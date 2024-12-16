# returns True if a year is leap, and False otherwise
def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else: 
        return False

years = [i for i in range(1900, 2101)]
leap_years = []

for i in years:
    if isLeap(i):
        leap_years.append(i)
    
print(leap_years)

months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

# returns the number of days of a given month in a given year
def numberOfDays(month, year):
    if isLeap(year) and month == "February":
        return months["February"] + 1
    else:
        return months[month]
    
# print(numberOfDays("January", 2009))
# print(numberOfDays("February", 2016))
# print(numberOfDays("February", 2015))
# print(numberOfDays("December", 2024))

# returns the day of the year of a given day, month and year
def day_of_the_year(day, month, year):
    sume = 0
    for i in months:
        if i != month:
            if isLeap(year) and i == "February":
                sume += months[i] + 1
            else:
                sume += months[i]
        else:
            sume += day
            return sume

# print(day_of_the_year(1, "March", 2024))
# print(day_of_the_year(31, "December", 2023))
# print(day_of_the_year(14, "October", 2001))

    
