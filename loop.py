finsh = false
while not finish:

    print()
    print("logic and, x to exit")
    s1 = input("Enter number a")
    s1 = input("Enter number b")
    s1 = input("Enter number c")
    if s1 == 'x' or s2 == 'x' or s3 =='x':
        finish = True
    else:
        try:
            a = int(s1)
            b = int(s2)
            c = int(s3)
            
            if a>b and a>c:
                print("a is greater")
            elif b>a and b>c:
                print("b is greater")
            elif c>a and c>b:
                print("c is greater")
            else
                print("No number is greater")

        except ValueError

                print("Error in number")
                
        
