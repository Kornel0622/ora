from data import cars
from os import system

filename = 'cars.csv'
cimsor = ''

def menu():
    system('cls')
    print('0 - Kilépés')
    print('1 - Új autó felvétele')
    print('2 - Listázás')
    print('3 - Autó törlése')
    return input('Kérem válasszon:')

def loadCars():
    file = open(filename, 'r', encoding='utf-8')
    global = file.readline() # címsor
    for row in file:
        splitted = row.strip().split(';')
        cars[splitted[0]] = int(splitted[1])

def addNewCar(car, performance):
    system('cls')
    print('Új autó')
    car = input('Autó típusa: ')
    performance = input('Teljesítménye:')
    cars[car] = performance
    saveCarToFile(car, performance)
    input('Autó felvétele. Tovább (Enter)... ')

def saveCarToFile(car, performance):
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'{car};{performance}\n')
    file.close()

def printAllCar():
    system('cls')
    print('Autók listája')
    for key, value in cars.items():
        print(f'{key} - {value}HP.')
    input('Tovább (Enter)...')

def deleteCar(car):
    system('cls')
    print('Autó törlése')
    car = input('A törlendő autó típusa: ')
    if car in cars:
        cars.pop(car)
        saveAllToFile()
        input('Autó törölve. Tovább(Enter)...')
    else:
        input('Nincs ilyen autó. Tovább (Enter)...')

def saveAllToFile():
    file = open(filename, 'w', encoding='utf-8')
    
    file.write(cimsor)
    for car,performance in cars.items():
        file.write(f'{car};{performance}\n')

    file.close