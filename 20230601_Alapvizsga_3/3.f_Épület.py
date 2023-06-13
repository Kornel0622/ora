class Épület:
    def __init__(self,sor:str):
        splitted=sor.split(';')
        self.nev=splitted[0]
        self.varos=splitted[1]
        self.orszag=splitted[2]
        self.magassag=float(splitted[3].replace(',','.'))
        self.emelet=int(splitted[4])
        self.epult=int(splitted[5])
    
épület:list[Épület]=[]

file = open('legmagasabb.txt','r', encoding='utf-8')
file.readline()
for row in file:
    épület.append(Épület(row.strip()))
file.close()

print(f'3.2 feladat: Épületek száma: {len(épület)} db')

emeletossz = 0
for item in épület:
    emeletossz+=item.emelet
print(emeletossz)

legmagasabb = épület[0]
for item in épület:
    if item.magassag > legmagasabb.magassag:
        legmagasabb = item
print(legmagasabb.nev)

for item in épület:
    if item.orszag == 'Olaszország':
        print('Van ilyen')
        break
else:
    print('nincs')



