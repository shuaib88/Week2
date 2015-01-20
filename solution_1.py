#Program finds the nth fibonnaci number. (Assuming - 1st fib is 1, 2nd is 1, 3rd is two)



def fibonnaci():
    n = eval(input("Which nth fibonnaci number would you like to find?? "))

    if n == 0:
        current_fib = 0
        
    elif n == 1:
        current_fib = 1

    elif n == 2:
        current_fib = 1

    elif n > 2: 

        prev_fib = 1
        current_fib = 2
        
        for i in range(n-3):
            holding = current_fib
            current_fib = prev_fib + current_fib
            prev_fib = holding

        print(current_fib)
    
fibonnaci()


#serendipitously a friend posted this fibonnaci inspired art to my facebook wall!!!
#http://bit.ly/1y7xfTW
