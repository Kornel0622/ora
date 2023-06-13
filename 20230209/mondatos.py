def capitalize(sentence:str):
    splitted = sentence.split(' ')
    newSentence = ''
    for item in splitted:
        newSentence = item.capitalize() + ' '
    return newSentence.strip()

sentence = input('Kérek egy mondatot:')
print(f'A nagybetűsített mondat: {capitalize(sentence)}')
