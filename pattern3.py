#!/bin/python

'''
1
12
123
1234
12345
'''

def pattern3(n):
    i=1
    for i in range(n+1):
        for j in range(i):
            print("%d" %(j+1),end='')
        print()
n=eval(input("enter n value"))
pattern3(n)

