import random

firstLetter = input("Enter a letter")
secondLetter = input("Enter another letter: ")
answer = firstLetter + 5*secondLetter
print(answer) 

repeat = random.randint(5,12)
print(repeat)

for counter in range(repeat):
    print("Hello")

nameList= []
name = input("Enter your name")

for letter in name:
    nameList.append(letter)

print(nameList) 
random.shuffle(nameList) 
print(nameList) 

anagram = ""
for counter in range(len(nameList)):
    anagram += nameList[counter]
    
print(anagram) 
print(anagram[0:1])

start_letter =""
for counter in range(6):
    random.shuffle(nameList)
    print(nameList)
    start_letter += nameList[0]

