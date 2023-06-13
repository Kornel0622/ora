def interspace(word):
    newWord = ''
    for letter in word:
        newWord+= letter + ' '
    return newWord



word = input('Kérek egy szót: ')
print(f'A ritkított szó: {interspace(word)}')