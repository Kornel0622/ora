from data import students
studentFile = 'students.txt'

def menu():
    choice = ''
    print('-----------------------')
    print('0 - Kilép')
    print('1 - Új tanuló felvétele')
    print('2 - Tanuló listázása')
    #print('3 - Tanulók beolvasása fájlból')
    #print('4 - Tanulók beolvasása')
    choice = input('Válasszon egy menüpontot: ')
    return choice

def newStudent():
    print('Új tanuló felvétele')
    name = input('Kérem a tanuló nevét: ')
    print('Tanuló sikeresen felvételre került.')

def showStudents():
    print('Tanulók listája')
    for student in students:
        print(f'\t{student}')

def saveToFile():
    file = open(studentFile, 'w', encoding='utf-8')
    file.write(student + '\n')
    print('Sikeres mentés.')

def saveToFile():
    file = open(studentFile, 'w', encoding='utf-8')
    for student in students:
        file.write(student + '\n')
    file.close()
    print('Sikeres mentés.')

def loadFromFile():
    file = open(studentFile, 'r', encoding='utf-8')
    for row in file:
        students.append(row.strip())
    file.close()
    print('Sikeres betöltés.')

def loadFromFile()