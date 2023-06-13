# dobjunk 2 dobokockaval egyszerre,
# addig amig mind2 6-os nem lesz

# végtelen ciklus
# több soros komment
#while 5 > 2:
 #   print('5 nagyobb mint a kettő')


from random import randint  

dobas = dobas2 = 0

while not (dobas1 == 6 and dobas2 == 6):
    dobas1 = randint(1,6)
    dobas2 = randint(1,6)
    print(f'Dobások eredménye:, {dobas1},{dobas2}')