"""
    TEJADA, MIKAYLA M.
"""

import sys

listClass = []

class Classes:
    classroom = ""
    cName = ""
    Units = ""
    prereq = []

    def __init__(self, room, name, unit, preq):
        self.classroom = room
        self.cName = name
        self.Units = int(unit)
        self.prereq = preq

class Admin:
    idnum = ""
    Name = ""

    def __init__(self, idnumber, name):
        self.idnum = idnumber
        self.Name = name

    def createClass(self, room, cname, units, preq):
        newClass = Classes(room, cname, units, preq)
        listClass.append(newClass)

    def removeClass(self, classes):
        listClass.remove(classes)
        
class Student:
    idnum = ""
    Name = ""
    UnitLim = ""
    CurrUnit = ""
    listclasses = []
    pastclass = []
    index = 0

    def __init__(self,idnumber, name, ulim):
        self.idnum = idnumber
        self.Name = name
        self.UnitLim = int(ulim)
        self.CurrUnit = 0
        self.index = 0
    
    def takeClass(self, classes):
        self.listclasses.append(classes)
        self.index += 1 
        self.CurrUnit += classes.Units
        
    def dropClass (self,classes):
        self.listclasses.remove(classes)
        self.index -= 1
        self.CurrUnit -= classes.Units


def validID():
    while True:
        idnum = input("ID Number: ")
        if idnum =="":
            sys.exit()
        elif idnum.isdigit()==0:
            print("Input valid ID Number. No letters or special characters.")
            continue
        elif int(idnum)>0 and int(idnum)<100000000:
            return int(idnum)
        else:
            print("Input valid ID Number. It should not exceed 100000000.")
            continue
        
def validPass():
    while True:
        password = input("Password: ")
        if len(password)>=8:
            return 1
        else:
            print("Password should have a minimum of 8 characters.")
            continue

def userType():
    while True:
        choice = input("[A] Student or [B] Admin: ")
        if choice=='A' or choice=='a':
            return 1
        elif choice=='B' or choice=='b':
            return 2
        else:
            print("Input valid choice.")
            continue
        
def displayclasses(listC):
    x = 0
    if len(listC)==0:
        print("No listed classes.")
        return 0
    else:
        print("Classes: ")
        print("No. \t Class Name \t Units \t Room")
        for x in range(len(listC)):
            print(x+1, "\t", listC[x].cName, "\t", listC[x].Units,"\t", listC[x].classroom)
        return 1

def checkRegClass(student, classchoice):
    x=0
    while(x<student.index):
        if student.listclasses[x].cName==classchoice.cName:
            return 0
        x+=1
    return 1

def checkSameClass(classname, room):
    x = 0
    while (x < len(listClass)):
        if (listClass[x].cName==classname and listClass[x].classroom==room):
            return 0
        x+=1
    return 1

def askDecision():
    while True:
        ans = input("Are you sure? \n[A] Yes \n[B] Cancel\n")
        if ans=='A' or ans=='a':
            return 1
        elif ans=='B' or ans=='b':
            return 0
        else:
            print("Invalid choice.")
            continue
    
def adminOption(admin):
    while True:
        choice = input("[A] Create class \n[B] Remove class \n[C] Log out\n")
        if choice=='A' or choice=='a':
            #create class
            pqlist = []
            while True:
                cname = input("Class name: ")
                if len(cname)==7 and cname.isdigit()==0:
                    break
                else:
                    print("Class name should have 7 characters including letters.")
                    continue
            while True:
                unit = input("Units: ")
                if (unit.isdigit()):
                    break
                else:
                    print("Input valid number.")
                    continue
            room = input("Room: ")
            while True:
                pqnum = input("Number of Prerequisites: ")
                if pqnum.isdigit()==0:
                    print("Input valid number.")
                    continue
                elif pqnum!='0':
                    x = 0
                    while (x < int(pqnum)):
                        pq = input("Prerequisite {}:" .format(x+1))
                        if (len(pq)==7):
                            y = 0
                            found = 0
                            if pq.isdigit():
                                print("Class name should include letters")
                                continue
                            elif pq == cname:
                                print("Class cannot be a prerequisite of itself.")
                                continue
                            else:
                                while y < len(pqlist):
                                    if pq == pqlist[y]:
                                        found = 1
                                    y+=1
                                if (found):
                                    print("Entered class is already in list of prerequisites.")
                                    continue
                                else:
                                    pqlist.append(pq)
                                    x+=1
                        else:
                            print("A class name should have 7 characters.")
                            continue
                    break
                else:
                    pqlist.clear()
                    break
	    #check if may katulad na na class
            if (checkSameClass(cname, room)):
                sure = askDecision()
                if (sure):
                    admin.createClass(room, cname, unit, pqlist)
                    print(listClass[len(listClass)-1].cName, "is successfully created.")
                else:
                    print("Cancelled.", cname, "was not created.")
                while True:
                    choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                    if choice2=='A' or choice2=='a':
                        adminOption(admin)
                        return 1
                    elif choice2=='B' or choice2=='b':
                        start()
                        break
                    else:
                        print("Invalid choice.")
                        continue
            else:
                print("Class already exists")
                while True:
                    choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                    if choice2=='A' or choice2=='a':
                        adminOption(admin)
                        return 1
                    elif choice2=='B' or choice2=='b':
                        start()
                        break
                    else:
                        print("Invalid choice.")
                        continue
        elif choice=='B' or choice=='b':
            #remove class
            numclass = displayclasses(listClass)
            if (numclass):
                while True:
                    remove = input("Enter the corresponding number of the class you want to remove: ")
                    if (remove.isdigit()==0):
                        print("Input a valid number.")
                        continue
                    elif int(remove)>0 and int(remove)<=len(listClass):
                        c = listClass[int(remove)-1].cName
                        sure = askDecision()
                        if (sure):
                            admin.removeClass(listClass[int(remove)-1])
                            print(c, "is successfully removed.")
                        while True:
                            choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                            if choice2=='A' or choice2=='a':
                                adminOption(admin)
                                return 1
                            elif choice2=='B' or choice2=='b':
                                start()
                                break
                            else:
                                print("Invalid choice.")
                                continue
                    else:
                        print("Chosen number is not on the list.")
                        while True:
                            choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                            if choice2=='A' or choice2=='a':
                                adminOption(admin)
                                return 1
                            elif choice2=='B' or choice2=='b':
                                start()
                                break
                            else:
                                print("Invalid choice.")
                                continue   
                return 1
            else:
                while True:
                    choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                    if choice2=='A' or choice2=='a':
                        adminOption(admin)
                        return 1
                    elif choice2=='B' or choice2=='b':
                        start()
                        break
                    else:
                        print("Invalid choice.")
                        continue
            
        elif choice=='C' or choice=='c':
            #logout
            start()
            break;
        else:
            print("Input valid action.")
            continue
            
def studentOption(student):
    while True:
        choice = input("[A] Add class \n[B] Drop class \n[C] View classes \n[D] Log-out\n")
        if choice=='A' or choice=='a':
            #add class
            numclass = displayclasses(listClass)
            if numclass==0:
                while True:
                    choice2 = input("Log out? [A] Yes or [B] No \n")
                    if choice2=='A' or choice2=='a':
                        start()
                        break
                    elif choice2=='B' or choice2=='b':
                        studentOption(student)
                        return 1
                    else:
                        print("Invalid choice.")
                        continue
            else:
                #choose class to take
                while True:
                    add = input("Enter the corresponding number of the class you wish to take: ")
                    if add.isdigit()==0:
                        print("Input a valid number.")
                        continue
                    elif int(add)>0 and int(add)<=len(listClass):
                        class2add = int(add)
                        #check muna if di pa nagreregister for that class
                        canAdd = checkRegClass(student, listClass[class2add-1])
                        if canAdd==1:
                            #not yet registered
                            #check if units will not exceed unit limit
                            if (student.CurrUnit + listClass[class2add-1].Units) <= student.UnitLim:
                                sure = askDecision()
                                if (sure):
                                    student.takeClass(listClass[class2add-1])
                                    print(listClass[class2add-1].cName, "is successfully added to your list of classes")
                                while True:
                                    choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                                    if choice2=='A' or choice2=='a':
                                       studentOption(student)
                                       return 1
                                    elif choice2=='B' or choice2=='b':
                                        start()
                                        break
                                    else:
                                        print("Invalid choice.")
                                        continue
                            else:
                                print("Taking class failed. You only have ", student.UnitLim-student.CurrUnit, " units allowed.")
                                while True:
                                    choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                                    if choice2=='A' or choice2=='a':
                                        studentOption(student)
                                        return 1
                                    elif choice2=='B' or choice2=='b':
                                        start()
                                        break
                                    else:
                                        print("Invalid choice.")
                                        continue
                        else:
                            #already registered
                            print("You are already enrolled for chosen class.")
                            while True:
                                choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                                if choice2=='A' or choice2=='a':
                                    studentOption(student)
                                    return 1
                                elif choice2=='B' or choice2=='b':
                                    start()
                                    break
                                else:
                                    print("Invalid choice.")
                                    continue
                            return 1
                    else:
                        print("Chosen number is not in the list.")
                        while True:
                            choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                            if choice2=='A' or choice2=='a':
                                studentOption(student)
                                return 1
                            elif choice2=='B' or choice2=='b':
                                start()
                                break
                            else:
                                print("Invalid choice.")
                                continue
        elif choice=='B' or choice=='b':
            #drop class
            allowToDrop = displayclasses(student.listclasses)
            if (allowToDrop):
                while True:
                    toDrop = input("Enter the corresponding number of the class you want to drop: ")
                    if toDrop.isdigit()==0:
                        print("Input a valid number.")
                        continue
                    elif int(toDrop)>0 and int(toDrop)<=len(student.listclasses):
                        remove = student.listclasses[int(toDrop)-1]
                        sure = askDecision()
                        if (sure):
                            student.dropClass(student.listclasses[int(toDrop)-1])
                            print(remove.cName, "is successfully dropped.")
                        while True:
                            choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                            if choice2=='A' or choice2=='a':
                                studentOption(student)
                                return 1
                            elif choice2=='B' or choice2=='b':
                                start()
                                break
                            else:
                                print("Invalid choice.")
                                continue
                    else:
                        print("Chosen number is not on the list.")
                        while True:
                            choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                            if choice2=='A' or choice2=='a':
                                studentOption(student)
                                return 1
                            elif choice2=='B' or choice2=='b':
                                start()
                                break
                            else:
                                print("Invalid choice.")
                                continue   
                return 1
            else:
                while True:
                    choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                    if choice2=='A' or choice2=='a':
                        studentOption(student)
                        return 1
                    elif choice2=='B' or choice2=='b':
                        start()
                        break;
                    else:
                        print("Invalid choice.")
                        continue
        elif choice=='C' or choice=='c':
            #view classes
            displayclasses(student.listclasses)
            while True:
                choice2 = input("Back to main menu? [A] Yes or [B] Log out\n")
                if choice2=='A' or choice2=='a':
                    studentOption(student)
                    return 1
                elif choice2=='B' or choice2=='b':
                    start()
                    break;
                else:
                    print("Invalid choice.")
                    continue
            return 1
        elif choice=='D' or choice=='d':
            #logout
            start()
            break;
        else:
            print("Input valid action.")
            continue

def start():
    print("ENLISTMENT SYSTEM\n")
    print("To terminate, press Enter")
    idnum = validID()
    validPass()
    uType = userType()

    if uType==1:
        #student
        while True:
            name = input("Name: ")
            if name.isalpha():
                break
            else:
                print("Input valid name.")
                continue
        while True:
            units = input("Unit Limit: ")
            if units.isdigit()==0:
                print("Input a valid number.")
                continue
            elif int(units)>=12 and int(units)<=21:
                break
            else:
                print("Unit limit is invalid. Min:12 Max:21")
                continue
        user = Student(idnum, name, units)
        studentOption(user)
    else:
        #admin
        while True:
            name = input("Name: ")
            if name.isalpha():
                break
            else:
                print("Input valid name.")
                continue
        user = Admin(idnum, name)
        adminOption(user)

#these two subjects are already created at the beginning of the problem
listClass.append(Classes("G201", "GEMATMW", 3, []))
listClass.append(Classes("G208", "CSMATH2", 3, ["BASMATH"]))

start()


"""
    NOTES:
    class with different classrooms are considered different
    id number cannot have letters and should be less than 100000000
    password should have a minimum of 8 characters
"""
