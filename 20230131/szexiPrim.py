from prim import prim

def szexiPrim(szam1, szam2):
    if abs(szam1 - szam2) != 6:
        return False
    else:
        if prim(szam1) == False or prim(szam2) == False:
            return False
        else:
            return True


szam1 = int(input('Kérek egy számot: '))
szam2 = int(input('Kérek egy számot: '))
if (szexiPrim(szam1, szam2) == True):
    print(f'({szam1},{szam2}) szexi primek')
else:
    print(f'({szam1},{szam2}) NEM szexi primek')