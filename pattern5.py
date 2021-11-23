#!/bin/python

'''
55555
4444
333
22
1
'''

def pattern5(n):
    i=n
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("%d" %i,end='')
        print()
n=eval(input("enter n value"))
pattern5(n)

