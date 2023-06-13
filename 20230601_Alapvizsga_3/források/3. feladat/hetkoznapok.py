def maganHangzokSzama(nap):
    maganhangzok = 'aáeéiíoóöőuúüű'
    darab = 0
    for item in nap:
        if item in maganhangzok:
            darab += 1
    return darab


napok = ['Hétfő','Kedd','Szerda','Csütörtök','Péntek']

maxNap = napok[0]
for item in napok:
    if maganHangzokSzama(item)>maganHangzokSzama(maxNap):
        maxNap = item
print(f'Alegtöbb magánhangzó a {maxNap}-ben van.')