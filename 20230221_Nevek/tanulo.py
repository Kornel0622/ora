class tanulo:
    def __init__(self, sor:str) -> None:
        splitted = sor.split(';')
        self.ev = int(splitted[0])
        self.osztaly = splitted[1]
        self.nev = splitted[2]
    def nevHossz(self):
        return len(self.nev.replace(' ',''))

    def azonosito(self):
        splitted = self.nev.split(' ')
        vezeteknev = splitted[0]
        keresztnev = splitted[1]
        azon = str(self.ev)[-1] + self.osztaly + vezeteknev[:3]
        return azon.lower()
