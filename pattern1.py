#!/bin/python

'''
*
**
***
****
*****
'''
def pattern_one(n):
    i=0
    j=0
    for i in range(n+1):
        for j in range(i):
            print("*",end=' ')
        print("\n")
n=eval(input("enter the number"))
pattern_one(n)

