#!/bin/python

def calci(a,b,c):
    if (c=='+'):
        return a+b
    elif (c=='-'):
        return a-b
    elif (c=='*'):
        return a*b
    elif (c=='/'):
        return a/b
    elif (c=='%'):
        return a%b
    else:
        return "invalid operation"
a,b,c=[eval(x) for x in input("enter two numbers and operator").split()]
print("the outcome of operation is",calci(a,b,c))


