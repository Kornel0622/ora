from data import autok
from Auto import Auto

def feltolt():
    a = Auto('AA-BB-123',150, 'Metál Piros', 2022 )
    # a.rendszam = 'AA-BB-123'
    # a.gyartasiEv = 2022
    # a.szin = 'Metál Piros'
    # a.teljesitmeny = 150
    autok.append(a)

def AutoBeker():
    a = Auto()
    print('Adja meg az auto adatait:')
    a.rendszam = input('Rendszám: ')
    a.gyartasiEv = input('Gyartasi ev: ')
    a.szin = input('Szín: ')
    a.teljesitmeny = input('Teljesítmény: ')
    autok.append(a)

def AutoKiir(auto):
    print(f'Rendszam: {auto.rendszam}, Gyartási év: {auto.gyrtasiEv}, Szín: {auto.szin}, Teljesítmény: {auto.teljesitmeny}')

def OsszesAutoKiir():
    for auto in autok:
        AutoKiir(auto)


#AutoBeker()
feltolt()
print(autok)
