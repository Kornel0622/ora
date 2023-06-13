from Car import Car
from data import cars

def loadFromFile(filename):
    cars = []
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        newCar = Car(row)
        cars.append(newCar)
    
def printCars(car):
    for cars in cars:
        print(f'{car.PlateNumber} - {car.Brand}')

def countCars():
    return len(cars)