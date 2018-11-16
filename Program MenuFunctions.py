def ShowMenu():
    print()
    print()
    print("(A)dd two numbers")
    print("(D)ivide one number by another")
    print("(Q)uit")
    print("> ",end="")

def GetNumber():
    Number = int(input("Enter a number between 0 and 10 "))
    while Number not in range(0,11):
        Number = int(input("Enter a number between 0 and 10 "))
    return Number

def Add():
    Number1 = GetNumber()
    Number2 = GetNumber()
    print("The sum of your numbers is", Number1 + Number2)

def Divide():
    Number1 = GetNumber()
    Number2 = GetNumber()
    print(Number1, "divided by", Number2, "is", Number1 / Number2)

Choice = ""
while Choice != "Q":
    ShowMenu()
    Choice = input()
    print()
    if Choice == "Q":
        print("bye")
    elif Choice == "A":
        Add()
    elif Choice == "D":
        Divide()
    else:
        print("Invalid choice, please try again ")
