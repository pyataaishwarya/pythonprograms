#!/bin/python

'''
def bigger_of_two(a,b):
    if(a>b):
        return a
    return b
a,b=[eval(x) for x in input("enter the two numbers").split()]
print("the biggest of two numbers is %d" %(bigger_of_two(a,b)))
'''

a,b=[eval(x) for x in input("enter two numbers").split()]
big = a if a>b else b
print("biggest number is %d" %big)
