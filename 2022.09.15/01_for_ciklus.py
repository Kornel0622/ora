# irjuk ki 1 es 100 kozoott a paros szamokat

for i in range(1, 101):
    # % - maradekos osztas, az osztas maradekat adja vissza
    # pl. 9 % 2 -> 1
    if i % 2 == 0:
        print(i)
# irjuk ki 1 es 100 kozott a paros szamokat
# masik megoldas
for i in range(1,101,2):
    print(i)
# irjuk ki 10 es 100 kozott a harommal oszthato szamokat
for i in range(10,101):
    if i % 3 == 0:
        print(i)


# masik megoldas
for i in range( 12,101,3):
    print(i)