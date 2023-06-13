from Player import Player

players : list[Player] = []

file = open('fob2016.txt','r',encoding='utf-8')
for row in file:
    players.append(Player(row.strip()))
file.close()

print(f'3. feladat: Játékosok száma: {len(players)}')

countWomen = 0
for item in players:
    if item.category == 'Noi':
        countWomen += 1
print(f'4. feladat: A női versenyzők aránya: {countWomen/len(players)*100:.2f}%')

winnerWomanPoints = -1
winnerWoman = ''
for item in players:
    if item.category == 'Noi' and item.totalPoints() > winnerWomanPoints:
        winnerWomanPoints = item.totalPoints()
        winnerWoman = item

print('6. feladat: A bajnok női versenyzők')
print(f'\tNév: {winnerWoman.name}')
print(f'\tEgyesület: {winnerWoman.team}')
print(f'\tÖsszpont: {winnerWoman.totalPoints()}')

file = open('osszpontFF.txt', 'w',encoding='utf-8')
for item in players:
    if item.category == 'Felnott ferfi':
        file.write(f'{item.name};{item.totalPoints()}\n')
file.close()

stats = {}
for item in players:
    if item.team in stats.keys():
        stats[item.team] += 1
    else:
        stats[item.team] += 1

print('8. feladat: Egyesület statisztika')
for key,value in stats.items():
    if key != 'n.a.' and value > 2:
        print(f'{key} - {value} fő')

print('9. feladat')
nevek = {}
for item in players:
    if item.firstname in stats.keys():
        stats[item.firstname] += 1
    else:
        stats[item.firstname] += 1
for key, value in nevek.items():
    print(f'\t {key} - {value}')