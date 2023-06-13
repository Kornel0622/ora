from toto import Fogadasi_fordulo

fordulo : list[Fogadasi_fordulo]=[]

file = open('toto.txt', 'r', encoding='utf-8')
file.readline()
for sor in file:
    fordulo.append(Fogadasi_fordulo(sor.strip()))
file.close()

print('3. feladat: Toto')
print('3.1 feladat: Adatok beolvasása és tárolása')
print(f'3.2 feladat: Fogadási fordulók száma: {len(fordulo)}')

telitalalatosDarab = 0
for item in fordulo:
    telitalalatosDarab += item.T13p1
print(f'3.3 feladat: Telitalalatos szelvények száma {telitalalatosDarab} darab')

for item in fordulo:
    if 'X' not in item.Eredmények:
        print('3.4 feladat: Volt döntetlen mentes forduló')
        break
else:
    print('3.4 feladat: Nem volt döntetlen mentes forduló')