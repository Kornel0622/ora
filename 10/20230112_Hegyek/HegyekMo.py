from mountain import *

mountains: list[mountain] = []

def readFromFile(fileName):
    file = open(fileName, 'r', encoding='utf-8')
    file = open(fileName, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        m = mountain(row)
        mountains.append(m)
    file.close()

def avgHeight():
    sum = 0
    for mnt in mountains:
        sum += mnt.height
    return sum/len(mountains)

def heighestMountain():
    maxIndex = 0
    for i, mnt in enumerate(mountains):
        if mnt.height > mountains[maxIndex].height:
            maxindex = i
    return maxIndex

def higherExist(height):
    for mnt in mountains:
        if height < mnt.height:
            return True
    return False



def main():
    readFromFile('hegyekMo.txt')
    print(f'3. feladat: Hegycsúcsok száma: {len(mountains)} db')
    print(f'4.feladat: Hegycsúcsok átlagos magassága: {avgHeight()}')
    print(f'5. feladat: A legmagasabb hegycsúcs adatai: ')
    highest = heighestMountain()
    print(f'Név: {mountains[highest].name}')
    print(f'Hegység: {mountains[highest].mountainRange}')
    print(f'Magasság: {mountains[highest].height}')
    height = input('6. feladat: Kérek egy magasságot')
    if higherExist(height) == True:
        print(f'Van ennél magasabb hegycsúcs')
    else:
        print(f'Nincs ennél magasabb hegycsúcs')
main()