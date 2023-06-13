from kocka import kockaFelszin, kockaTerfogat
from gomb import gombFelszin, gombTerfogat

def FelszinVagyTerfogat():
    valasz = ''
    while valasz != 'f' and valasz != 't':
        valasz = input('Felszín vagy térfogat érdekli? (f/t): ')
    
    return valasz

def menu():
    valasz = ''
    while valasz != '1' and valasz != '2':
        print('\n0 - Kilépés')
        print('1 - Kocka felszín és térfogat számítás')
        print('2 - Gömb felszín és térfogat számítás')
        print('3 - Négyzet alapú gúla felszín és térfogat számítás')
        valasz = input('válasz: ')

    return valasz

valasz = menu()
if valasz == '1':
    a = float(input('A kocka oldala: '))
    if FelszinVagyTerfogat() == 'f':
        print(f'Térfogat: {kockaFelszin(a)}')
    else:
        print(f'Felszín: {kockaTerfogat(a)}')
elif valasz == '2':
    r = float(input('A gomb sugara: '))
    if FelszinVagyTerfogat() == 'f':
        print(f'Térfogat: {gombTerfogat(r)}')
    else:
        print(f'Felszín: {gombFelszin(r)}')
elif valasz == '3':
    a = float(input('A gúla alapjának oldala: '))
    magassag = float(input('A gúla magassága: '))
    if FelszinVagyTerfogat() == 'f':
        print(f'Térfogat: {negyzetesGulaTerfogat(a, magassag)}')
    else:
        print(f'Felszín: {negyzetesGulaFelszin(a, magassag)}')