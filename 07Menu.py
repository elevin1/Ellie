def hello(): #hello world funciton
    print("Hello World") 
def goodbye(): #goodbye world function
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")  
def person(): #what is your name function
    print("Hello")
    name = input("What is your name ? ")
    print("Goodbye", name)  
def teacher(): #teacher name function
    name = input("Teacher's name (try Mr Horan) ")
    if name == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print( name + " is an ok teacher")
def forloop():
    for x in range(1, 500):
        print(x)
def whileloop():
    while True:
        deez = input("What is the name of this subject ")
        if deez ==  "IST":
            print("")
            print("")
            print("Congratulations!!")
            print("")
            print("")
            break
        else: 
            print("Not Correct - try again")
def stringloop():
    stringname = input("What is your string? ")

    ran = len(stringname)

    for element in (range(0, ran)):
        print(stringname[element])
    
def invalid():
    print("invalid option")

def startofoutput(): 
    print("")
    print("----Start of Output ---------------------------")
    print("")
def endofoutput():
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")

while True:
    subject = input(""" 
 ------------------------------------------------
|                                                |
|    07Menu                                      |
|    Name : Ellie Liu                            |
|    Version : 01                                |
|                                                |
 ------------------------------------------------

1. Hello World
2. Goodbye World
3. Goodbye Person
4. Good Teacher
5. forLoop
6. whileLoop
7. string Loop
8. Convert to ascii
9. Encode a string
x. To Exit
Enter an option """)

    if subject == "1":
        startofoutput()
        hello()
        endofoutput()
        input("Press Enter to continue")
        
    elif subject=="2":
        startofoutput()
        goodbye()
        endofoutput()
        input("Press Enter to continue")

    elif subject=="3":
        startofoutput()
        person()
        endofoutput()
        input("Press Enter to continue")
    
    elif subject=="4":
        startofoutput()
        teacher()
        endofoutput()
        input("Press Enter to continue")

    elif subject=="5":
        startofoutput()
        forloop()
        endofoutput()
        input("Press Enter to continue")
    
    elif subject=="6":
        startofoutput()
        whileloop()
        endofoutput()
        input("Press Enter to continue")
    
    elif subject=="7":
        startofoutput()
        stringloop()
        endofoutput()
        input("Press Enter to continue")
    
    elif subject=="x":
        startofoutput()
        endofoutput()
        input("Press Enter to continue")
        break
    
    else:
        startofoutput()
        invalid()
        endofoutput()
        input("Press Enter to continue")

