number=int(input('enter a whole number:  '))
while number <0:
    print('type in a number above 0')
    number=int(input('enter a whole number:  '))
print(number)
result=number//2
print(result)
remainder=number%2
print(remainder)
binary=''

while number!=0:
    remainder=number%2
    binary+=str(remainder)
    number=number//2
print(binary)
binary=list[binary]
binary.reverse()
print(binary)
