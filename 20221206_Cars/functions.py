from Car import Car 
from data import cars

def loadFromFile(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        newCar = Car(row.strip())
        cars.append(newCar)

def printCars():
    for car in cars:
        print(f'{car.PlateNumber} - {car.Brand}')

def countCars():
    return len(cars)

def avgConsumption():
    sum = 0
    for car in cars:
        sum += car.Consumption
    return sum / countCars()

def avgPriceByBrand(brand):
    sum = 0
    count = 0 
    for car in cars:
        if brand == car.Brand:
            sum += car.Price
            count += 1
    return sum / count

def existsCarOverSpeedLimit(limit)->bool:
    for car in cars:
        if car.Speed >= limit:
            return True
    return False    

def searchCarAndGiveBackAllDataYouKnowAboutItButWhenItDidntExistDontGiveBackAnything(platenumber)
    for car in cars:
        if car.PlateNumber == platenumber:
            return car
    return False
