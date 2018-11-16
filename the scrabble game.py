def getname():
    name = input("Enter your name ")
    while len(name) <2:
        print("name is too short")
        name = input("Enter your name ")
    return name

getname()
        
    

