#!/bin/python

def remainder_quotient(n,d):
    i=1
    while(n>=d):
        n=n-d
        if (n<d):
             print("rem:%d" %n)
        i=i+1
    print("quo:%d" %(i-1))
n=eval(input("enter the numerator value"))
d=eval(input("enter the denamenator value"))
remainder_quotient(n,d)

