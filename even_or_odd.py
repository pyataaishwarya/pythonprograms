#!/bin/python

def even_odd(n):
    if (n%2==0):
        return 1
    return 0
n=int(input("enter the number"))
n1=even_odd(n)
if(n1==1):
    print("number is even :%d" %n)
else:
    print("number is odd :%d" %n)



