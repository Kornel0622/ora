from functions import loadFromFile, printCars, countCars, avgConsumption, avgPriceByBrand, existsCarOverSpeedLimit, countCarsBySpeed, searchCarAndGiveBackAllDataYouKnowAboutItButWhenItDidntExistDontGiveBackAnything

loadFromFile('autok.csv')
# printCars()
# print(f'A nyilvántartásban {len(cars)} darab autó van.')
print(f'A nyilvántartásban {countCars()} darab autó van.')
print(f'Volvo-k átlagárai: {round(avgPriceByBrand("Volvo"))}')
print(f'A nyilvántartásban szereplő autók fogyasztása {avgConsumption(): 3.2f}')
print(f'A nyilvántartásban szereplő autók fogyasztása {round(avgConsumption(), 2)}')
speedLimit = int(input('Mennyinél gyorsabb autókat számoljuk meg?: {countCarsBySpeed}'))
if existsCarOverSpeedLimit(speedLimit):
    print(f'A megadott sebességnél({speedLimit}) gyorsabb autók száma: {countCarsBySpeed}')
platenumber = input('Írjad be a rendszámot yooo')
result = searchCarAndGiveBackAllDataYouKnowAboutItButWhenItDidntExistDontGiveBackAnything()
if result == False:
    print('Gyaaa ilyen nincsen.')
else:
    print(f'Az autó adatai: ')
    print(f'\t Márka:{result.Brand}')
    print(f'\t ár:{result.Price}')
    print(f'\t év:{result.Year}')