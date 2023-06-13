# FELELŐSORSOLÓ
# kerjunk be neveket addig amig be nem irja hogy VÉGE
# taroljuk el a neveket egy listaban

from random import randint


diakok = []

nev = input('kérem a tanuló nevét: ')

# while not(nev == 'VÉGE'):
#while nev != 'VÉGE':
#    diakok.append(nev)
#    nev = input('kérem a tanuló nevét: ')

nev = ''
while nev != 'VÉGE':
    nev = input('kérem a tanuló nevét: ')
    if nev != 'VÉGE':
        diakok.append(nev)   

print(diakok)

# Sorsoljunk ki egy felelőt
if len(diakok)>0:
   feleloSorszama = randint(0,len(diakok)-1)
   print(f'A felelő: {diakok[feleloSorszama]}')
