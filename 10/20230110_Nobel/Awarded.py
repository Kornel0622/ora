class Awarded:
    def __init__(self, row:str) -> None:
        #év;típus;keresztnév;vezetéknév
        #2017;fizikai;Rainer;Weiss
        splitted = row.split(';')
        self.year = int(splitted[0])
        self.type = splitted[1]
        self.firstname = splitted[2]
        self.lastname = splitted[3]