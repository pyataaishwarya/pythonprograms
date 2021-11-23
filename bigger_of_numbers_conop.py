#!/bin/python

def biggest_of_four_numbers(a,b,c,d):
    big = a if (a>b) and (a>c) and (a>d) else b if (b>c) and (b>d) else c if (c>d) else d
    return big
a,b,c,d=[eval(x) for x in input("enter four numbers").split()]
print("biggest number is %d" %(biggest_of_four_numbers(a,b,c,d)))



