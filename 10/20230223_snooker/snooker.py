from player import player

players : list[player] = []

file = open('snooker.txt','r',encoding='utf-8')
file.readline()
for row in file:
    players.append(player(row.strip()))
file.close()

print(f'3.feladat: {len(players)} versenyző szerepel a világranglistán')

sum = 0
for item in players:
    sum += item.prize
print(f'4. feladat: A versenyzők átlagosan {sum / len(players):.2f} fontot kerestek.')

max = -99999
maxIndex = -1
for index,item in enumerate(players):
    if item.country == 'Kína' and max < item.prize:
        max = item.prize
        maxIndex = index
print('5. feladatW: A legjobban kereső kínai versenyző:')
print(f'\tHelyezés: {players[maxIndex].Position}')
print(f'\tNév: {players[maxIndex].name}')
print(f'\tOrszág: {players[maxIndex].country}')
print(f'\tNyeremény: {players[maxIndex].prize * 380:,} Ft')

norvegia = False
for item in players:
    if item .country == ' Norvégia':
        norvegia = True
if norvegia:
    print('6. feladat: A versenyzők között van norvég versenyző. ')
else:
    print('6. feladat: A versenyzők között nincs norvég versenyző. ')

for item in players:
    if item.country == 'Skócia':
        print('6+1. feladat: A versenyzők között van skót versenyző.')
        break
else:
    print('6+1. feladat: A versenyzők között van Skót veresenyző.')


stats = {}
for item in players:
    if item.country in stats.keys():
        stats[item.country] += 1
    else:
        stats[item.country] = 1

print('7. feladat: Statisztika')
for key,value in stats.items():
    print(f'\t{key} - {value}')

