from szamok import szamok, feltolt, megszamlalas

print(f'A számok között{megszamlalas()} darab pozitív van.')
print(f'A pozitiv szamok atlaga{pozitivAtlag()}')
print(F'A legnagyobb szám: {legnagyobb()}')
print(f'A legkisebb szám: {legkisebb()}')
keresendo = int(input('Kérek egy számot: '))
if eldontes (keresendo):
    print('A megadott szám benne van a listában. ')
    print(f'A megadott szám sorszáma: {kereses(keresendo)+1}')
else: 
    print('A megadott szám NINCS a listában.')