from random import randint

print('Melyik lottó legyen?')
print('1 - Ötöslottó')
print('2 - Hatos  lottó')
print('3 - Skandináv lottó')
valasz = input('Válasz (1-3):')
if valasz == '1':
    LEGNAGYOBB_SZAM = 45
    SZAMOK_DB = 6
elif valasz =='2':
    LEGNAGYOBB_SZAM = 45
    SZAMOK_DB = 6
elif valasz == '3':
    LEGNAGYOBB_SZAM = 35
    SZAMOK_DB = 7
else:
    print('Hibás válasz, alapértelmezett: Ötös lottó')
    LEGNAGYOBB_SZAM = 90
    SZAMOK_DB = 5

lottoszamok = []

if SZAMOK_DB > LEGNAGYOBB_SZAM:
    print('Lehetetlen a megadott adatokkal lottószámokat generálni!')
else:
    while len(lottoszamok) < SZAMOK_DB:
        szam = randint(1, LEGNAGYOBB_SZAM)
        if szam not in lottoszamok:
            lottoszamok.append(szam)

lottoszamok.sort()
print('Az e heti nyrőszámok emelkedő számsorrendben: ', lottoszamok)