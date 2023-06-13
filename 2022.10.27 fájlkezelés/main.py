from functions import menu, newStudent, showStudents, saveToFile, loadFromFile
students = []

choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        newStudent()
    elif choice == '2':
        showStudents()
    #elif choice == '3':
    #    saveToFile()
    #elif choice == '4':
    #    loadFromFile()
