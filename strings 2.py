name=input("Enter your name ")

surname=input("Enter your surname ")

username=surname[:3] + name[:1] + str(len(surname))

print(username)

