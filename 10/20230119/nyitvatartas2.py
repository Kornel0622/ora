from math import *
ido = input('Mennyi idő van most?(óó:pp)')
splitted = ido.split(':')
ora = int(splitted[0])
perc = int(splitted[1])
osszesPerc = ora * 60 + perc
if ora >= 8 and ora < 16:
    print('A bolt nyitva van!')
    maradekOra =  floor((16 * 60 - osszesPerc) / 60)
    maradekPerc = 60 -(osszesPerc % 60)
    if maradekPerc == 60:
        maradekPerc = 0
    print(f'Ennyi időd van még odaérni:{maradekOra}óra {maradekPerc}perc')
else:
    print('A bolt zárva van!')