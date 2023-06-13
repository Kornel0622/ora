body = int(input('Kérem a súlyt kilogrammban: '))
height = int(input('Kérem a magasságot cm-ben: '))
TTI = body / height **2 *10000
print(f'A testtömeg indexe: {TTI:.2f}')

if TTI <16:
    print('A testsúly osztálya: súlyos soványság') 
if TTI >= 30:
    print('A testsúly osztálya: elhízás')
if TTI > 16 and TTI < 18.49:
    print('A testsúly osztálya: soványság')    
if TTI > 18.5 and TTI < 18.49:
    print('A testsúly osztálya: normális')
if TTI > 25 and TTI < 29.99:
    print('A testsúly osztálya: elhízás')    



