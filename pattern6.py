#!/bin/python

'''
5
44
333
2222
11111
'''

def pattern6(n):
    for i in range(n+1,0,-1):
        for j in range(n+1,i,-1):
            print("%d" %i,end='')
        print()
n=eval(input("enter n value"))
pattern6(n)

