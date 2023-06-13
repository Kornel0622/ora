from re import I
from names import students

def printStudents():
    for student in students:
        print(student)

def printStudentsWithNumbers():
    for i in range(len(students)):
        print(f'{i+1}. {students[i]}')

def printReverseStudents():
    for i in range(len(students)-1, -1, -1):
        print(f'{i+1}. {students[i]}')

def existsStudent(nameToSearch): # < - formalis parameter
    for student in students:
        if students == nameToSearch:
            return True
    return False

    def searchStudent(nameToSearch):
        for i in range(len(students)):
            if nameToSearch == students[i]:
                return i
        return False


#A leghosszabb nevű tanuló
def longestNameLenght():
    longest = len(students[0])
    longestName = students[0]
    for student in students:
        if len(student) > longest:
            longest = len(student)
            longestName
    return longest

def searchNeamesBylength(length):
    for student in students:
        if length == len(student):
            return student
    return False

def averageNameLength():
    sum = 0
    for student in students: 
        sum += len(student)
    return round(sum / len(students), 1)