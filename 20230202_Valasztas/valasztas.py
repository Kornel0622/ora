from ember import Ember

emberek: list[Ember] = []

file = open('szavazatok.txt', 'r', encoding='utf-8')
for sor in file:
    emberek.append(Ember(sor))
file.close()



def keres(nev):
    for item in emberek:
        if item.teljesNev == nev:
            return item
    return False

print(f'2. feladat: A választáson {len(emberek)} képviselőjelölt indult.')

nev = input(f'3. feladat: Kéviselő neve: ')
eredmeny = keres(nev)
if eredmeny == False:
    print('Ilyen nevű képviselő nem szerepel a nyilvántartásban!')
else:
    print(f'\tA jelölt a {eredmeny.kerulet}-s számú körzetben indult')
    print(f'\tA kapott szavazatok száma: {eredmeny.szavazatokSzama}')

osszesSzavazat = 0
for item in emberek:
    if item in emberek:
        osszesSzavazat += item.szavazatokSzama

atlag = (osszesSzavazat / 12 345) * 100

print(f'4. feladat: A választáson {osszesSzavazat} szavazó a jogosultak {}%-a vett részt.')

max = 0 
for item in emberek:
    if max < item.szavazatokSzama
        max = item.szavazatokSzama

print('5. feladat: A legtöbb szabvazat: {max}}')