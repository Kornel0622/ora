# Olvasson be egy dátumot és függvény(ek) segítségével döntse el, hogy a dátum helyes-e

def leapYear(year):
    if year % 4 != 0:
        return False
    if year %100 == 0 and year %400 != 0:
        return False
    return True

def checkDate(date:str):
    splitted = date.split('.')
    year = int(splitted[0])
    month = int(splitted[1])
    day = int(splitted[2])
    if month > 12 or month < 1:
        return False
    if len(splitted) != 3:
        return False
    days = [31, 28, 31, 30, 31 ,30 ,31, 31, 30, 31, 30, 31]
    if days[month - 1] < day:
        return False
    if month == 2 and leapYear(year) == False and day > 28:
        return True

date = input('Kérek egy dátumot: ')
if checkDate(date) == True:
    print('A dátum helyes!!!!!!!')
else:
    print('rósz')