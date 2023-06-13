szelesseg = int(input('Hány méter széles a terület?'))
hossz = int(input('Hány méter hosszú a terület?'))
print('A felszántadó terület:')
meret = int(input(f'Mérete (m2) : {szelesseg * hossz}'))
ol = (0,2780364289)
meret2 = { szelesseg * hossz * ol}
input(f'Mérete (négyszögöl): {meret2}')
fizetes = (7 / 100 + 5000)
dij = int(input(f'Munkadíj: {szelesseg * hossz / ol * fizetes} Ft.'))

