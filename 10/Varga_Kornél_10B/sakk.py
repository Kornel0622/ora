class Sakk:
    def __init__(self, row:str) -> None:
        splitted = row.split()
        self.azonosito = int(splitted[0])
        self.nev = splitted[1]
        self.orszag = splitted[2]
        self.nem = splitted[3]
        self.elopont = int(splitted[4])
        self.szuletesev = int(splitted[5])

