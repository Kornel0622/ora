class player:
    def __init__(self, row) -> None:
        splitted = row.split(';')
        self.Position = int(splitted[0])
        self.name = splitted[1]
        self.country = splitted[2]
        self.prize = int(splitted[3])

        