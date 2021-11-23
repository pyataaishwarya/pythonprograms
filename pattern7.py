#!/bin/python

'''
5
54
543
5432
54321
'''

def pattern7(n):
    for i in range(n,0,-1):
        for j in range(n,i-1,-1):
            print("%d" %j,end='')
        print()

n=eval(input("enter n value"))
pattern7(n)

