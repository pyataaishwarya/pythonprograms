#!/bin/python

'''
1
23
456
78910
1112131415
'''

def pattern8(n):
    k=1
    for i in range(n+1):
        for j in range(i):
            print("%d " %k,end='')
            k=k+1
        print()
n=eval(input("enter n value"))
pattern8(n)

