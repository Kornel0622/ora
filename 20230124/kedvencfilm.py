from math import *
def óraperc(perc):
    ora = floor(perc / 60)
    perc = perc % 60
    return str(ora) + ' óra ' + str(perc) + ' perc '

for i in range(3):
    cim = input('Add meg egy film címét!')
    hossz = int(input('Hány perces a film?'))
    print(f'A/Az {cim} című film {óraperc(hossz)} hosszú.')