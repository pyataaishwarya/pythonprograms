#!/bin/python

def fibonacci_series(n):
    x=1
    y=1
    print("%d\t%d\t" %(x,y),end='')
    for i in range(n-2):
        z=x+y
        print("%d\t" %z,end='')
        x=y
        y=z
n=eval(input("enter value of n"))
fibonacci_series(n)

