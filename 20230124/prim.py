def prim(szam):
    if szam == 1:
        return False
    for i in range(2szam):
        if szam % i == 0:
            return False
    return True

for i in range(1, 101):
    if prim(i):
        print(f'{i}', end=' ')
