#!/bin/python

'''
1
22
333
4444
55555
'''

def pattern(n):
    i=1
    j=1
    for i in range(n+1):
        for j in range(i):
            print("%d" %i,end='')
        print()
n=eval(input("enter n value"))
pattern(n)

