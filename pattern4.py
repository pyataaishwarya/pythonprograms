#!/bin/python

'''
1
01
101
0101
10101
'''

def pattern4(n):
    i=1
    for i in range(n+1):
        for j in range(i):
            if ((i+j+1)%2==0):
                print("1", end='')
            else:
                print("0",end='')
        print()
n=eval(input("enter n value"))
pattern4(n)

