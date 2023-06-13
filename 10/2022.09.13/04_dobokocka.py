# generáljunk egy véletlen számot 1 és 6 között
# dobjunk 5-ször
# mennxyi a dobások átlaga?

from random import randint

atlag = 0
for i in range(5):
    dobas = randint(1,6)
    atlag += dobas
    print(dobas)
    
print(f'A dobások átlaga: {atlag / 5}')