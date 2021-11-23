#!/bin/python

def multiplication(a,b):
    i=1
    mul=0
    while(i<=b):
        mul=mul+a
        i=i+1
    return mul
a=eval(input("enter the first number"))
b=eval(input("enter the second number"))
print("result is %d" %(multiplication(a,b)))


