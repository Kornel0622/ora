from Awarded import Awarded

awardedList : list[Awarded] = []

awardedList = []

def readFromFile(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        a = Awarded(row.strip())
        awardedList.append(a)
    file.close()

# awardedList[10] -> object Awarded osztály egy példánya
# awardedList[10].firstname

def searchByName(name):
    for awarded in awardedList:
        if awarded.firstname + ' ' + awarded.lastname == name:
            return awarded
    return False

def searchByTypeAndYear(type, year):
    for awarded in awardedList:
        if awarded.year == year and awarded.type == type:
            return awarded
    return False

def awardedSinceYear(year):
    print('Az {} év után az alábbi emberek kaptak béke Nobel-díjat.')
    for awarded in awardedList:
        if awarded.year >= year and awarded.type == 'béke':
            print(f'\t{awarded.firstname} {awarded.lastname}')
    else: 
        print(f'{year}-ban/ben az {type} Nobel-díjat kapott: {result.firstname} {result.lastname}')

typesOfAwards = {}

def stat():
    for awarded in awardedList:
        if awarded.type in typesOfAwards.keys():
            typesOfAwards[awarded.type] += 1
        else:
            typesOfAwards[awarded.type] = 1



def main():
    readFromFile('nobel.csv')
    result = searchByName('Arthur B. McDonald')
    print(f'Arthur B. McDonald {result.type} Nobel-díjat kapott, az alábbi évben: {result.year}. ')
    year = (input('adja meg az évet: '))
    type = input('adja meg a díj típusát: ')
    result = searchByTypeAndYear(type, year)
    if result == False:
        print('Nincs találat')
    else:
        print(f'{year}-ben az {type} Nobel-díjat kapott: {result.firstname} {result.lastname}')
    awardedSinceYear(1990)
    stat()
    print(f'Nobel-díj fajtáinak a száma:')
    for key, value in typesOfAwards.items():
        print(f'\t{key} - {value}')

main()