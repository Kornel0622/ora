from feladat import *

def resztvettek():
        return len(names)

def legalabb():
    win = 8600
    pont = 0
    összes = 0
    for pont in points:
        if pont > win:
            összes += 1
    return összes

def gyoztesPont():
    max = 0
    pont = 0
    for pont in points:
        if pont > max:
            max = pont
    return max