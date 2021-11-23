#!/bin/python

def bigger_of_four_numbers(a,b,c,d):
    if ((a>b) and (a>c) and (a>d)):
        return a
    elif ((b>c) and (b>d)):
        return b
    elif (c>d):
        return c
    else:
        return d
a,b,c,d=[eval(x) for x in input("enter four numbers").split()]
print("the biggest of four numbers is %d" %(bigger_of_four_numbers(a,b,c,d)))



