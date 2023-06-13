ora = int(input('Hány óra van most?'))
if ora >= 8 and ora < 16:
    print('A bolt nyitva van!')
    print(f'Ennyi időd van még odaérni: {16-ora}')
else:
    print('A bolt zárva van!')