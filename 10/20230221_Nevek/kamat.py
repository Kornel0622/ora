# Készitsen fv-t ami kamatos kamatot számol
# paraméterek: összeg, hónapok száma, éves kamat
#Pl: 1000000 Ft, 18 hónap, évi 16%
def kamatosKamat(osszeg, honapokSzama, evesKamat):
    evekSzama = honapokSzama / 12
    return osszeg * (1 + evesKamat/100)**evekSzama

osszeg = int(input('Mennyi a  befektetett összeg?: '))
honapok = int(input('Mennyi hónapra kíván befektetni?: '))
kamat = float(input('Mennyi az éves kamat?: '))

print(f'A kamattal növelt érték a lejárati idő után: {kamatosKamat(osszeg, honapok, kamat)} ')
