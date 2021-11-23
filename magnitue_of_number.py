#!/bin/python

def magnitude_of_number(n):
    mag = n if n>0 else (~n+1)
    return mag
n=int(input("enter the number"))
print("magnitude of number is %d" %(magnitude_of_number(n)))


