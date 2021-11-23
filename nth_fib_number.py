#!/bin/python

'''
def fibonacci(n):
    if (n==1):
        return 0
    if (n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=eval(input("enter n value"))
print("the nth fibonacci number is",fibonacci(n))
'''
def fibonacci(n):
    a=0
    b=1
    if (n<0):
        print("incorrect output")
    elif (n==0):
        return a
    elif (n==1):
        return b
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return b
n=eval(input("enter n value"))
print("the nth fibonacci number is",fibonacci(n))


