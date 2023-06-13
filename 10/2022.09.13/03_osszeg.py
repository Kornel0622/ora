# Kérjünk be 10 darab számot
# majd írjuk ki az összeget

# for ciklus
# i - ciklusváltozó
# range(10) generál egy tartományt 0-tól 9-ig
# i - ciklusváltozó (lépésenként felveszi a tartomány minden elemét)
osszeg = 0
for i in range(10):
  szam = int(input('Kérek egy számot: '))
  # osszeg = osszeg + szam 
  # szamoljuk ki a jobb oldali kifejezes erteket 
  # majd annak erteket rakjuk be a bal oldali valtozoba
  osszeg += szam

print(f'A számok összege: {osszeg}')