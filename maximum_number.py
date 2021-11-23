#!/bin/python

'''
def maximum(a,b):
    return max(a,b)
a=eval(input("enter a value"))
b=eval(input("enter b value"))
print("maximum of {} and {} is {}".format(a,b,maximum(a,b)))
'''

def maximum(a,b):
    if (a>b):
        return a
    else:
        return b
a=eval(input("enter a value"))
b=eval(input("enter b value"))
print("maximum of {} and {} is {}".format(a,b,maximum(a,b)))


