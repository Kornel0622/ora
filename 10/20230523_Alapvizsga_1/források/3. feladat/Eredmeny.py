class Eredmeny:
    def __init__(self,sor:str):
        splitted= sor.split(';')
        self.nev = splitted[0]
        self.rajtszam = splitted[1]
        self.kategoria = splitted[2]
        self.ido = splitted[3]
        self.szaz = int(splitted[4])
        
        splittedIdo = self.ido.split(':')
        self.idoOraban = int(splittedIdo[0]) + int(splittedIdo[1])/60 + int(splittedIdo[2])/3600