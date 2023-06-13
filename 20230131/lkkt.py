szam1 = 127
szam2 = 394
for i in range(szam1, szam1*szam2, szam1):
    if szam2 % i == 0:
        print(i)