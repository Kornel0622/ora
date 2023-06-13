from functions import loadFromFile, showResults, menu, showCompetitors, addResult, deleteResult


choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        showCompetitors()
        input()
    elif choice == '2':
        showResults()
    elif choice == '3':
        addResult()
    elif choice == '4':
        deleteResult()



#loadFromFile()
#showCompetitors()
#showResults()