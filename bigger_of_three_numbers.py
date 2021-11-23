#!/bin/python

'''
def bigger_of_three(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    return c
a,b,c=[eval(x) for x in input("enter three numbers").split()]
print("the bigger number is %d" %(bigger_of_three(a,b,c)))
'''

a,b,c=[eval(x) for x in input("enter three numbers").split()]
big = a if a>b and a>c else b if b>c else c
print("bigger number is %d" %big)


