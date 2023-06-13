from mukorcsolya import atlagAlattiDb, atlagPontszam, gyoztes, gyoztesVersenyzo, pontszamGeneral, versenyzok

pontszamGeneral()
print(versenyzok)
print(f'Agyőztes pontszáma: {gyoztes()}')
print(f'A győztes versenyző rajtszáma: {gyoztesVersenyzo()+1}')
print(f'A versenyzők átlag pontszáma: {atlagPontszam()}')
print(f'Átlag alatti versenyzők száma: {atlagAlattiDb()}')