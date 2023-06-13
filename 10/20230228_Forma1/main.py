from pilotak import Pilota

pilots : list[Pilota] = []

file = open('pilotak.csv','r',encoding='utf-8')
file.readline()
for row in file:
    pilots.append(Pilota(row.strip()))
file.close()

print(f'3. feladat: {len(pilots)}')

#pilots[-1]
#pilots[len(pilots)]
print(f'4. feladat: {pilots[-1].name}')

print('5. feladat:')
for item in pilots:
    if item.year < 1901:
        print(f'\t{item.name} ({item.birthDate})')

min = 999999
minIndex = -1
for index,item in enumerate(pilots):
    if item.number != '':
        number = int(item.number)
        if number < min:
            min = number
            minIndex = index

print(f'6. feladat: {pilots[minIndex].name} - {pilots[minIndex].country}')

stat = {}
for item in pilots:
    if item.number in stat.keys():
        stat[item.number] += 1
    else:
        stat[item.number] = 1
print('7. feladat:', end='')
first = True
for key,value in stat.items():
    if key != '' and value > 1:
        if first != True:
            print(key, end=' ')
            first = False
        else:
            print(f'{key}', end='')
            first = False