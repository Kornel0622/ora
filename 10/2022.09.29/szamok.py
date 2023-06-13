from random import randint


szamok = []

def feltolt():
    for i in range(randint(5,25)):
        szamok.append(randint(0,100))

# szamoljuk meg, hogy hany pozitiv szam van
def megszamlalas():
    darab = 0
    for szam in szamok:
        if szam > 0:
            darab += 1
    return darab

# szamoljuk ki a pozitív számok átlagát
def pozitivAtlag():
    osszeg = 0
    for szam in szamok:
        if szam > 0:
            osszeg += szam
    return osszeg / megszamlalas

def legnagyobb():
    max = szamok[0]
    for szam in szamok:
        if max < szam:
    return max 

#melyik a legkisebb szám?
def legkisebb():
    min = szamok[0]
    for szam in szamok:
        if min > szam:
            max = szam
    return min

def eldontes():
    for szam in szamok:
        if szam == keresettSzam:
            return True
    return False 

#keressuk meg, hogy egy szam hanyadik a listaban! (valasz: indexe vagy False)
def kereses(keresettSzam):
    for i in range(len(szamok)): # i értéke: 0, 1, 2, 3...
        if szam[i] == 
             return i
        return False

    