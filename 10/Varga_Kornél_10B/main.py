from sakk import Sakk

sakkos : list[Sakk] = []

file = open('sakk.txt','r',encoding='utf-8')
file.readline()
for row in file:
    sakkos.append(Sakk(row.split()))
file.close()

print(f'4.feladat: Versenyzők száma: {len(sakkos)}')
