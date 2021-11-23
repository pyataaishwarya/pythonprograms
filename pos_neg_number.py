#!/bin/python

def positive_negative(n):
    if (n>0):
        return 1
    elif (n<0):
        return 2
    else:
        return 3
n=int(input("enter the number"))
n1=positive_negative(n)
if (n1==1):
    print("number is positive %d" %n)
elif(n1==2):
    print("number is negative %d" %n)
else:
    print("number is equal to zero %d" %n)


