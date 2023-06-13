from leap_year import leap_year

def nextDay(date:str):
    splitted = date.split('-')
    year = int(splitted[0])
    month = int(splitted[1])
    day = int(splitted[2])
    
    daysOfmonth = [31,28,31,30,31,30,31,31,30,31,30,31]

    if leap_year(year) == True:
        daysOfMonth[1] = 29

    day += 1
    if (day> daysOfMonth[month-1]):
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1

date = input('Kérek egy dátumot (éééé-hh-nn):')
print(f'A következő nap:{nextDay(date)}')
