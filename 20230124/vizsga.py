def check(point):
    if point >= 48:
        return True
    else:
        return False
name = 'asd'

while not name == '':
    name = input('Add meg a vizsgázó nevét! ')
    if name != '':
        point = int(input('Add meg a pontszámát!'))
        if check(point) == True:
            print(f'{name} vizsgája sikeres.')
        else:
            print(f'{name} vizsgája sikertelen.')

