#!/bin/python

def factorial(n):
    if (n==0)or(n==1):
        return 1
    else:
        return n*factorial(n-1)
n=eval(input("enter n value"))
print("factorial of {} is {}".format(n,factorial(n)))
'''
def factorial_of_number(n):
    fact=1
    i=1
    while(i<=n):
        fact=fact*i
        i=i+1
    return fact
n=eval(input("enter the number"))
print("factorial of given number is %d" %(factorial_of_number(n)))

'''
