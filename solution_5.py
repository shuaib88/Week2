## prime checker


def primechecker():
    n = eval(input("What number do you want to check if prime? "))
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

primechecker()
