from tanulo import tanulo

tanulok : list[tanulo] = []
    
def azonositoKereso(azonosito):
    for item in tanulok:
        if item.azonosito() == azonosito:
            return item
        return False


file = open('nevek.txt','r',encoding='utf-8')
for item in file:
    sor = sor.strip()
    tanulok.append(tanulo(sor())) 
file.close()

print(f'3. feladat: Az iskolába {len(tanulok)} tanuló jár.')

leghosszabb = tanulok[0].nevHossz()
for item in tanulok:
    if leghosszabb < item.nevHossz():
        leghosszabb = item.nevHossz()

print(f'4. feladat: A leghosszabb ({25}karakter) nevű tanuló(k):')
for item in tanulok:
    if leghosszabb == item.nevHossz():
        print(f'\t{item.nev}')
    
print(f'5. feladat: Azonosítók:')
print(f'\tElső: {tanulok[0].nev} - {tanulok[0].azonosito()}')
print(f'\tUtolsó: {tanulok[-1].nev} - {tanulok[-1].azonosito()}')

azonosito = input('6. feladat: Kérek egy azonosítót [pl.: 4dvavkri]: ')
tanulo = azonositoKereso(azonosito)
if tanulo == False:
    print('Nincs megfelelő tanuló.')
else:
    print(f'{tanulo.ev} {tanulo.osztaly} {tanulo.nev}')