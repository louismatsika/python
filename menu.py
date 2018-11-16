def getTri():
    base = (int(input("Enter the base of the triangle "))
    height = (int(input("Enter the height of the triangle "))
    triangle1 = (base * height) / 2
    print("The area of the triangle is ", triangle1)


def getRec():
    length = (int(input("Enter the length of the rectangle "))
    width = (int(input("Enter the width of the rectangle "))
    rectangle1 = length * width
    print("The area of the rectangle is", rectangle1)


def getTra():
    top = (int(input("Enter the top of the trapezium "))
    base = (int(input("Enter the base of the trapezium "))
    height = (int(input("Enter the height of the trapezium: "))
    trapezium1 = ((top + base) / 2) * height
    print("The area of the trapezium is", trapezium1)

end = False
while not end:
   
    print("Menu")
    print()
    print("1) Area of Triangle")
    print("2)  Area of Rectangle")
    print("3)  Area of Trapezium")
    print("4) Exit")
    print()

    choice = input("Select an option")
    print()
    if choice == "1":
        getTri()
        print()
    elif choice == "2":
        getRec()
        print()
    elif choice == "3":
        getTra()
        print()
    elif choice == "4":
        end = True
    else:
        print("Invalid Selection")
        print()
