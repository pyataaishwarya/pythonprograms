#!/bin/python

def multiplication_table(n):
    i=1
    while(i<=10):
        print("%d*%d=%d\n" %(n,i,n*i))
        i=i+1
n=eval(input("enter number"))
multiplication_table(n)
