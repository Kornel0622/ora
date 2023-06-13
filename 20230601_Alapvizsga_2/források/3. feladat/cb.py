from CBadás import CBadás

adások : list[CBadás] = []

file = open('cb.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    adások.append(CBadás(row.strip()))

file.close()

print('3. feladat: CB-rádió')
print(f'3.2 feladat: Bejegyzések száma: {len(adások)} db')

sanyiDarab = 0
for item in adások:
    if item.Nev == 'Sanyi\n':
        sanyiDarab += 1
print(f'3.3 feladat: Sanyihoz tartozó bejegyzések száma: {sanyiDarab} db')

maxAdas = adások[0]
for item in adások:
    if item.AdasDb > maxAdas.AdasDb:
        maxAdas = item

print('3.4 feladat: A legtöbb adás')
print(f'\tIdő: {maxAdas.Ora}:{maxAdas.perc} Darab: {maxAdas.AdasDb} Név:{maxAdas.Nev}')

for item in adások:
    if item.AdasDb == maxAdas.Adasdb:
        print(f'\tIdő: {item.Ora}:{item.Perc} Darab: {item.AdasDb} Név: {item.Nev}')

file = open('cb2.txt', 'w', encoding='utf-8')
file.write('Kezdés;Nev;AdasDb\n')
for item in adások:
    file.write(f'{item.Ora*60+item.Perc};{item.Nev};{item.AdasDb}\n')
file.close()

stat = {}
for item in adások:
    if item.Nev in stat.keys():
        stat[item.Nev] += item.AdasDb
    else:
        stat[item.Nev] = item.AdasDb

print('3.6 feladat: Statisztika')
for key,value in stat.items():
    print(f'\'{key}: {value} db')