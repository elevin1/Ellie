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
def stringLoop ():
    print

def startofoutput(): 
    print("----Start of Output ---------------------------")
    print("")
def endofoutput():
    print("")
    print("----End of Output -----------------------------")

i=0

while i==0:
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Ellie Liu                            |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")

#1-9 quesitons
    subject = input(""" 
1. Hello World
2. Goodbye World
3. Goodbye Person
4. Good Teacher
5. forLoop
6. whileLoop
7. string Loop
8. Convert to ascii
9. Encode a string
Enter an option """)

#results for the user input

    if subject == "1":
        startofoutput()
        hello()
        endofoutput()
        input("Press enter to continue")
        continue
            
    elif subject == "2":
        startofoutput()
        goodbye()
        endofoutput()
        input("Press enter to continue")

    elif subject == "3":
        startofoutput()
        person()
        endofoutput()
        input("Press enter to continue")
    
    elif subject == "4":
        startofoutput()
        teacher()
        endofoutput()
        input("Press enter to continue")

    elif subject == "5":
        startofoutput()
        forloop()
        endofoutput()
        print("")
        input("Press enter to continue")
    



