from data import names, jumps
filename= 'jumps.csv'

def menu():
    print('0 - Kilép')
    print('1 - Versenyzők')
    print('2 - Összes eredmény')
    print('3 - Új eredmény felvétele')
    print('4 - Törlés')
    return input('Választás:')

def loadFromFile():
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
    
        splitted = row.strip().split(';')
        print(splitted)
        names.append(splitted[0])
        jumps.append(float(splitted[1]))
    file.close

def showCompetitors():
    for name in names:
        print(f'\t{name}')
        input()

def showResults():
    system('cls')
    print('Eredmények')
    for i in range(len(names)):
        print(f'\t{names[i]} - {jumps[i]}m.')
    input()

def addResult():
    system('cls')
    print('Új eredmény felvétele')
    name = input('Név: ')
    jump = float(input('Ugrás hossza: '))
    names.append(name)
    jumps.append(jump)
    print('Sikeres felvétel.')
    input()

def saveResultToFile(name, jump):
    file = open(filename, 'a', )
    file.write(f'{name};{jump}\n')
    file.close()

def searchName(needle):
    for index,name in names:
        if name == needle:
            return index 
    return False

def deleteResult():
    system('cls')
    print('Eredmény törlése')
    name = input('Ki legyen törölve:')
    names.remove(name)
    index = searchName(name)
    names.pop(index)
    jumps.pop(index)
    print(f'{name} törölve.')
    input()

def saveAll():
    file = open(filename, 'w', encoding='utf-8')
    for index in range(len(names)):
        file.write(f'{name};{jump}\n')
        file.close()