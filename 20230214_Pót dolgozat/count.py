def countVowels(text:str):
    count = 0
    vowels = ['a,á,e,é,i,í,o,ó,ö,ő,u,ú,ü,ű']
    for letter in text.lower():
        if letter in vowels:
            count += 1
    return count

text = input('Kérek egy szöveget: ')
print(f'A szövegben a magánhangzók száma: {countVowels(text)}')



