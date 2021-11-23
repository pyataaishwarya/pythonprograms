#!/bin/python

def power_of_number(a,n):
    p=1
    i=1
    while(i<=n):
        p=p*a
        i=i+1
    return p
a=eval(input("enter the base of the number"))
n=eval(input("enter the power of the number"))
print("a to the power n value is %d" %(power_of_number(a,n)))

'''
def power(a,n):
    p=1
    for i in range(n):
        p=p*a
    return p
a=eval(input("enter the base of a number"))
n=eval(input("enter the power of a number"))
print("a to the power n is %d" %(power(a,n)))

'''
