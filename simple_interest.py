#!/bin/python

def si(p,t,r):
    i=(p*t*r)/100
    return i
p,t,r=[eval(x) for x in input("enter principle,time and rate").split()]
print("simple interest is %f"%(si(p,t,r)))


