from math import pi

count = int(input('Hány gömböt akarsz kiszámolni?:'))
for i in range(count):
    sugar = float(input(f'Adja meg a(z) {i+1} gömb sugarát: '))
print(f'\tA gömb térfogata: {round(4 * sugar * sugar * pi, 2)} ')
print(f'A gömb térfogata: {4 * pow(sugar,3) * pi / 3:.2f}')
