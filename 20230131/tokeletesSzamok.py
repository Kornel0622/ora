def tokeletes(szam):
    osszeg = 0
    for i in range(2, szam / 2):
        if szam % i == 0:
            osszeg += i
    if osszeg == szam:
        return True
    else:
        return False


for i in range(10):
    bekertSzam = int(input(f'Kérem a(z) {i+1}. számot: '))
if tokeletes(bekertSzam) == True:
    print(f'{bekertSzam} tökéletes.')
else:
    print(f'{bekertSzam} nem tökéletes.')