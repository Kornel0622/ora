def LNKO(szam1, szam2):
    if szam1 < szam2:
        kisebb = szam1
    else:
        kisebb = szam2
    for i in range(szam1, 1, -1):
        if szam1 % i == 0 and szam2 % i == 0:
            return i

szam1 = int(input('Kérek egy számot: '))
szam2 = int(input('Kérek mégegy számot: '))
print(f'LNKO({szam1},{szam2}) = {LNKO(szam1,szam2)}')

