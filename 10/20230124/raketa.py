time = int(input('Hány órás visszaszámlálást tervezünk? '))
totalTime = time
for i in range(time, 0, -1):
    print(f'Visszaszámlálás: {i}')
    choose = input('Fel kell függeszteni a visszaszámlálást, (i/n)?')
    if choose == 'i':
        totalTime += 1
print(f'A rakéta a visszaszámlálást követően ennyi órásval indult: {totalTime}')
