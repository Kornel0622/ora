# taroljuk el 10 kocka dobas eredmenyet

from random import randint


dobasok = [] # lista adatszerkezet
#egyszerre tobb adat tarolhato
#az egyes adatokat szammal indexeljuk benne
#az index 0-tol indul

for i in range(10):
    #egyDobas = randint(1,6)
    #dobasok.append(egyDobas)

    dobasok.append(randint(1, 6))
    # az append() a lista vegehaz hozzarakja a megadott elemet

print(dobasok)

for item in dobasok:
# for ciklus végigmegy a lista elemein
# az egyes listaelemek egyesevel bekerulnek az item valtozoba
# item helyett barmilyen valtozonev hasznalhato
    print(item)

#az egyes listaelemek elerese  
# mi volt az 5. dobas
print('Az 5. dobás értéke: ', dobasok[4])

#csereljuk le a 9. dobast 6-ra
dobasok[8] = 6

print(dobasok)

#toroljuk ki a listabol az elso 6-ost
if 6 in dobasok:
    #in operator true-t ad vissza hogy az adott ertek benne van a listaban
    dobasok.remove(6)

print(dobasok)