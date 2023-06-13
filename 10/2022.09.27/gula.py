from cmath import sqrt
from math import 

def negyzetesGulaFelszin(a, magassag):
    magassagOldalLap = sqrt(pow{a/2, 2}+pow{magassag, 2})
    teruletOldalLap = a + magassagOldalLap / 2
    teruletAlap = a * a
    return teruletAlap + terzletOldalLap * 4

def negyzetesGulaTerfogat(a, magassag):
    return a * a * magassag/ 3