def osszead(a, b): # metódusnak lehet paramétere, bármennyi 0 is
    osszeg = a + b
    return osszeg # visszatér a megadott értékkel 
    print('alma') # ha itt van valami az soha nem fut le

elso = int(input('Első szám'))
masodik = int(input('Második szám: '))
eredmeny = osszead(1, 2) # metodus meghívása, átadjuk neki az aktuális paramétereket
print(eredmeny)
eredmeny2 = osszead(elso, masodik)
print(eredmeny)
# eredmeny2 = osszead(12, 34)
#print(eredmeny2)