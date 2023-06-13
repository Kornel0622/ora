from functions import aranyErem, legtobbEremIndexe, sportagErmekSzama, sportagakSzama, tobbMintEgyErem
from data import *
# Írja ki hány sportágban osztottak érmet az 1924-es Párizsi olimpián
print(f'{sportagakSzama()}darab sportágban osztottak érmet az 1924-es Párizsi olimpián.')

# Írja ki a képernyőre hány olyan sportág volt, ahol több, mint 1 érmet osztottak

print(f'{tobbMintEgyErem()}olyan sportág volt, ahol több, mint 1 érmet osztottakdarab olyan sportág volt, ahol több, mint 1 érmet osztottak')

# Írja ki a képernyőre összesen hány aranyérmet oszottak összesen
print(f'{aranyErem()}darab aranyérmet oszottak összesen')

# Írja ki a képernyőre, hogy melyik sportágból osztották a legtöbb érmet
print(f'{sportagak[legtobbEremIndexe()]}sportágból osztották a legtöbb érmet')

# Kérje be egy sportág nevét, és írja ki, hogy ebből a sportágból hány érmet osztottak
sportagNeve = input('Sportág neve: ')
ermmekSzama = sportagErmekSzama(sportagNeve)
if ermekSzama == False:
    print('Nincs ilyn sportág!')
else:
    print(f'{sportagNeve} sportágból {ermekSzama} érmet osztottak.')
