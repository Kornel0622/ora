class Pilota:
    def __init__(self, row:str) -> None:
        splitted = row.split(';')
        self.name = splitted[0]
        self.birth = splitted[1]
        self.country = splitted[2]
        self.number = splitted[3]  
        splittedYear = self.birthDate.split('.')
        self.Year = int(splittedYear[0])

                            