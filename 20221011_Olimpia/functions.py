from data import *

def sportagakSzama():
    return len(sportagak)


def tobbMintEgyErem():
    darab = 0
    for erem in ermekSzama:
        if erem > 1:
            darab += 1
    return darab

def aranyErem():
    osszeg = 0
    for erem in ermekSzama:
        osszeg += erem
    return osszeg

def legtobbEremIndexe():
    maxSorszam = 0 
    for i in range(len(ermekSzama)): #i: 0,1,2,3...
        if ermekSzama[i] > ermekSzama[maxSorszam]:
            maxSorszam = i
    return maxSorszam

def sportagErmekSzama(sportag: str):
    for i in range(len(sportagak)):
        if sportag.upper() == sportagak[i].upper:
            return ermekSzama[i]
    return False
