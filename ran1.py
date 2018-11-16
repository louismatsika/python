def menu():
    print()
    print()
    print("(1) Enter a qoute from a famous person")
    print("(2) Enter the title for a song")
    print("(2) Exit program")
    print()




loop=True

while loop==True:
    menu()
    print()
    option=input('Enter your option ')
    print()
    if option=="1":
        qoute=input('Enter your qoute... ')
        print()
        print(qoute.upper())
        print()
    for letter in qoute:
        
        
