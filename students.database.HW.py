## Students Databse
#  * data structures
#  * functional programming
#  * CRUD operations
#  * interactivity
#  * libs (random, faker)
#  * using "pip"
import random
import os
from faker import Faker
fake = Faker()

stud_names  = []   # str
stud_grades = []   # float
stud_years   = []   # int

def genStudents(amount = 10):
    for i in range(amount):
        stud_names.append( fake.name() )
        stud_years.append( random.randint(1,5) )
        stud_grades.append( round(random.uniform(5.0,10.0),2) )

def printStudents():
    for i in range(len(stud_names)):
        print("-"*42)
        #print(stud_names[i],stud_years[i],stud_grades[i])
        print(
            f"{stud_names[i]:30} | {stud_years[i]:2} | {stud_grades[i]}"
        )
    print("-"*42)

def addStudent():
    s_name = input("Enter new student name: ")
    s_year = int(input("Enter new student year: "))
    s_grade = float(input("Enter new student grade: "))

    stud_names.append(s_name)
    stud_years.append(s_year)
    stud_grades.append(s_grade)

def editStudent():
    s_name = input("Enter the name of the student whose data need to be edited: ")
    s_index = -1
    for i in range(len(stud_names)):
        if stud_names[i] == s_name:
            s_index = i
            break
    
    if s_index >= 0:
        data = input("What do you want to edit (year/grade): ")
        if data == "year":
            stud_years.pop(s_index)
            s_year = int(input("Enter edited student year: "))
            if s_year >= 1 and s_year <= 5:
                stud_years.insert(s_index,s_year)
        elif data == "grade":
            stud_grades.pop(s_index)
            s_grade = float(input("Enter edited student grade: "))
            if s_grade >= 5.0 and s_grade <= 10.0:
                stud_grades.insert(s_index,s_grade)
        elif data == "year and grade":
            stud_years.pop(s_index)
            stud_grades.pop(s_index)
            s_year = int(input("Enter edited student year: "))
            s_grade = float(input("Enter edited student grade: "))
            if s_year >= 1 and s_year <= 5:
                stud_years.insert(s_index,s_year)
            if s_grade >= 5.0 and s_grade <= 10.0:
                stud_grades.insert(s_index,s_grade)
            

def removeStudent():
    s_name = input("Enter the name of the student to delete: ")
    s_index = -1
    for i in range(len(stud_names)):
        if stud_names[i] == s_name:
           s_index = i 
           break

    if s_index >= 0:
        stud_names.pop(s_index)
        stud_years.pop(s_index)
        stud_grades.pop(s_index)

def findbStudent():
    s = -1
    max_grade = float(0)
    for i in range(len(stud_names)):
        if stud_grades[i] > max_grade:
            max_grade = stud_grades[i]
            s = i

    print("The best student is: " f"{stud_names[s]:30} | {stud_years[s]:2} | {stud_grades[s]}")    

def findrStudents():
    min = float(input("Enter the minimal grade: "))
    max = float(input("Enter the maximal grade: "))
    r_name  = []
    r_year  = []
    r_grade = []
    for i in range(len(stud_names)):
        if stud_grades[i] >= min and stud_grades[i] <= max:
            r_name.append(stud_names[i])
            r_year.append(stud_years[i])
            r_grade.append(stud_grades[i])

    for e in range(len(r_name)):
        print(f"{r_name[e]:30} | {r_year[e]:2} | {r_grade[e]}")


def printMenu():
    print("### STUDENTS DATABASE ###")
    print("1. Show students list")
    print("2. Add a student")
    print("3. Edit a student")
    print("4. Remove a student")
    print("5. Find the best student")
    print("6. Print data of students with the grades in the certain range")
    print("0. Exit")
    print("#########################")
    option = int(input(">>> "))
    return option

#############################################
genStudents(5)
while True:
    os.system("cls")
    option = printMenu()

    if option == 1:
        printStudents()
        input("hit enter to continue")
    elif option == 2:
        addStudent()
    elif option == 3:
        editStudent()
    elif option == 4:
        removeStudent()
    elif option == 5:
        findbStudent()
        input("hit enter to continue")
    elif option == 6:
        findrStudents()
        input("hit enter to continue")
    elif option == 0:
        break