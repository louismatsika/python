firstletter=input('enter a letter ')
secondletter=input('enter another letter ')
letters=[firstletter,secondletter,secondletter,secondletter]
print(letters)

namelist=[]
name=input('whats your name ')

for letter in name:
    namelist.append(letter)

print(namelist)
random.shuffel(namelist)
print(namelist)
