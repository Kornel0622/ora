# kérjunk be egy 1 es 10 kozotti szamot,
# ha nem jo akkor kerjuk be ujra, amig jo nem lesz

szam = 0 # olyan kezdoerteke legyen, hogy eloszor belementjuk a ciklusba
while szam > 10 or szam < 1:
    szam = int(input('kérek egy számot 1 és 10 között'))
    