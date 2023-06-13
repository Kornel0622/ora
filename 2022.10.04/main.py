from operator import index
from functions import *

#printStudentsWithNumbers()
#printReverseStudents()
name = input('Kérek egy nevet: ')
if existsStudent(name): # name < - aktualis parameter
    print('Létezik ilyen nevű tanuló')
    print(f'A tanuló sorszáma: {searchStudent(name)}')
else:
    print('Nem létezik ilyen nevű tanuló')
#index = searchStudent(name)
#if index != False:
#    print(f'A tanuló sorszáma: {index}')

print(f'A leghosszabb név: {searchNameByLength(longestName)[]}')
print(f'A leghosszabb név: {(longestName)[]}')

print(f'Az osztály tanulóinak nevének az átlagos hosszúsága: {averageNameLength()}')
