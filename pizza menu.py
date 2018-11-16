

    



print("               ~==========================~")
print("                 Welcome to our pizzaria!")
print("               ~==========================~")
print()
print("**************************************************************")
print("*todays deal:vegetarian and margarita pizzas 10% off together*")
print("**************************************************************")
print()
repeat = True

while repeat == True:
    choice = input("Please select one of the following options:\n\
     1.Pizza vegetarian \n \
    2.Pizza pepperoni\n \
    3.Pizza 3 cheeses\n \
    4.Pizza margarita\n \
    5.Exit\n\
    >>>")


    if choice == "1" or "Pizza vegetarian":
        print()
        print("Vegetarian: £8")
        print()
    elif choice == "2" or "Pizza pepperoni":
        print()
        print("Pepperoni: £12.80")
        print()
    elif choice == "3" or "Pizza 3 cheeses":
        print()
        print("3 cheeses: £10.5")
        print()
    elif choice == "4" or "Pizza margarita":
        print()
        print("Margarita: £7.82")
        print()
    elif choice == "5"  :
            repeat = False
    else:
        print()
        print("error: that is not a option, please try again")
        print()
        

        
        
