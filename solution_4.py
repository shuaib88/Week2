# This program gets a starting value from user and then prints
# the syracuse sequence for that starting value



def syracuseSeq():
    
    currentElement = eval(input("What integer would you like a syracuse sequence for? "))
    

    if isinstance(currentElement,int) == True:
    
        while currentElement > 1:        

            if currentElement%2 == 0:
    
                currentElement = currentElement / 2

                print(currentElement)
        
            else:

                currentElement = 3 * currentElement + 1

                print(currentElement)


    else:
        print("I'm sorry you didn't enter an integer, try it again dummy")


syracuseSeq()

