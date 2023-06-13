from functions import loadFromFile, printCars, countcars

cars = loadFromFile('auto.csv')
# printCars()
# print(f'A nyilvántartásban {len(cars)} darab autó')
print(f'A nyilvántartásban {countcars()} darab autó')