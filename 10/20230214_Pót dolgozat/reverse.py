def reverse(sentence:str):
    words = sentence.split(' ')
    newSentence = ''
    for word in words:
        newWord = ''
        for i in range(len(word)-1,-1,-1):
            newWord += word[i]
        newSentence += newWord + ' '
    return newSentence

sentence = ''
while sentence != 'VÉGE':
    sentence = input('Kérek egy mondatot: ')
    if sentence != 'VÉGE':
        print(f'A szöveg visszafele: {reverse(sentence)}')