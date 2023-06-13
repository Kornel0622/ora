from functions import *



#addNewCar('Toyota Supra',123)
#addNewCar('Delorian',234)
#addNewCar('Nissan GTR',536)

choice = ''
while choice != '0':
    choice = menu()
    if choice == '1':
        addNewCar()
    elif choice == '2':
        printAllCar()
    elif choice == '3':
        deleteCar('')