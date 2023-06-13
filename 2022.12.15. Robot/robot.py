from functions import *

command = input('Kérem a robot parancsai:').upper()

eCount = counter("E", command)
dCount = counter("D", command)
nCount = counter("N", command)
kCount = counter("K", command)


print(f'E betűk száma: {eCount}')
print(f'D betűk száma: {dCount}')
print(f'N betűk száma: {nCount}')
print(f'K betűk száma: {kCount}')

if eCount > dCount:
   eCount -= dCount
   dCount = 0
else:
    dCount -= eCount
    eCount = 0

if nCount > kCount:
   nCount -= kCount
   kCount = 0
else:
    kCount -= kCount
    nCount = 0

print(f'Egy legrövidebb út:  {"E" * eCount} {"D" * dCount} {"K" * kCount} {"N" * nCount}')