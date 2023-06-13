from data import *
from functions import avgArea, countOverAvg, searchCountry, smallestIndex, allSmallestIndex

print(f'Az országok száma: {len(countries)}')
#print(f'Az országok száma:{len(area)}')

#Számoljuk meg, hogy hány olyan ország van, ...
print(f'Az átlag területnél ({round(avgArea())} km2) nagyobb országok száma: {countOverAvg()}')

#legkisebb orszag
smallest = smallestIndex()
print(f'Alegkisebb ország: területe: {areas[smallest]} km2', end='. ')
print('\tEzek az országok: ')
for i in allSmallestIndex():
    #print(f'\t\t{countries[i]}')
    print(f'{countries[i]}', end=', ')
print()
#Kérjuk be egy orszag.................
country = input('Ország: ')
result = searchCountry(country)
if result == False:
    print('Nincs ilyen ország.')
else:
    print(f'Az ország területe: {areas[result]}')