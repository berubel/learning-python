from random import randint
from math import sqrt


def fibonacci(n):

    fib = []
    for i in range(1, n):
        if i <= 1:
            fib.append(1)
            fib.append(1)
        else:
            fib.append(fib[i-2] + fib[i-1])
        
    return fib

def rec_fibonacci(n):

    if n <= 1:
        return n
    else:
        return rec_fibonacci((n-1)) + rec_fibonacci(n-2)
    
def math_fibonacci(n):

    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
    

if __name__ == '__main__':

    n = randint(1,10)

    print(fibonacci(n))
    print(rec_fibonacci(n))
    print(math_fibonacci(n))


    # Print the fibonacci sequence until n
    # for i in range(1, n+1):
    #    print(math_fibonacci(i))
    #    print(rec_fibonacci(i))
     




