def displayMenu():
    print()
    print("MENU")
    print("====")
    print("1.Welcome Message")
    print("2. Pi")
    print("3. Cylinder")
    print("x. Exit")

def getPi():
    pi = 3.14
    return pi

def displayName(s1):
    print("Hello",s1)

def getCylinder(r,1):
    p = getPi()
    volume = p*r*l
    return volume

finish = false
while not finish:
    displayMenu()
    choice = input("Enter choise")

    if choice == '1':
        print()
        name = input("Enter your name")
        displayName(name)
    elif choice == '2':
        pi = getPi()
        print()
        print("Pi = ",Pi)
    elif choice == '3':
        print()
        s1 = input("Enter radius")
        s2 = input("Enter length")
        radius = int(s1)
        lenght = int(s2)
        volume = getCylinder(radius,length)
        print("Volume of cylinder =",volume)
    elif choice == 'x' or choice == 'X':
        finish = True
    else:
        print("Invalid choice")
