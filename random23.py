hi = True
import time
lower = False
xd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
while hi:
    s = input("Enter a string")
    for i in xd:
        if i in s:
            lower = True
        else:
            time.sleep(0.0001)
    if lower == True:
        print("Your string has lowercase letters")
    else:
        print("Your string does not have lowercase letters")
    lower = False
