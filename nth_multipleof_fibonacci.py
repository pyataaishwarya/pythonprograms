#!/bin/python

def findPosition(k,n):
    f1=0
    f2=1
    i=2
    while i!=0:
        f3=f1 + f2
        f1=f2
        f2=f3
        if f2%k==0:
            return n*i
        i=i+1
    return

n=eval(input("enter n value multipe number"))
k=eval(input("enter number of whose multiple we are finding"))
print("Position of n\'th multiple of k in"
      "Fibonacci Series is",findPosition(k,n))



