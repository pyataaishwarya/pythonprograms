#!/bin/python

def alphabet_case_reverse(c):
    if (c>=97 and c<=122):
        c=c-32
    elif (c>=65 and c<=90):
        c=c+32
    return c
c=int(input("enter the number"))
print("case reverse of character is %d" %(alphabet_case_reverse(c)))

