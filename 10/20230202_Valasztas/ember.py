class Ember:
    def __init__(self, row) -> None:
        splitted = row.split(' ')
        self.kerulet = splitted[0]
        self.szavazatokSzama = int(splitted[1])
        self.vezetekNev = splitted[2]
        self.keresztNev = splitted[3]
        self.part = splitted[4]
        self.nev = self.vezetekNev +' '+ self.keresztNev