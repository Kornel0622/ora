from torna import Torna

tornasz : list[Torna] = []

file = open('torna.csv','r',encoding='utf-8')
file.readline()
for row in file:
    tornasz.append(Torna(row.strip()))
file.close()

print(f'2. feladat: {len(tornasz)} versenyző')

max = 0 
maxIndex = 0
for index, item in enumerate(tornasz):
    if item.korlat > max:
        max = item.korlat
        maxIndex = index
print('3. feladat')
print(f'Korláton {tornasz[maxIndex].nev} szerezte meg az aranyermet')

print('4. feladat')
print(float(input('Kérem a versenyző rajtszámát: ')))
