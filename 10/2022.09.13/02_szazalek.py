# Kérjük be, az összes tanuló számát
# és azt, hogy hányan buktak meg az alapvizsgán
# hat

tanulokSzama = input(input('Tanulók száma: '))
bukottakSzama = ink(input('Bukottak száman: '))

atmaent = tanulokSzama - bukottakSzama

atmentSzazalek = atment / tanulokSzama * 100

print(f'Az átment tanulók százaléka: {atmentSzazalek}%')