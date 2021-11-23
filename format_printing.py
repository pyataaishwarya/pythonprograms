#!/bin/python

def format_number(n):
    y=n%10
    z=n/10
    w=z%10
    u=z/10
    v=u%10
    s=n/1000
    t=y*1000+w*100+v*10+s*1
    return y,s,s,n,t,w,v,u,z,v,w,z,u,s,y,n,s
n=int(input("enter the number"))
print("%d\t%d\t%d\t%d\t%d\n%d\t%d\t%d\t%d\n%d\t%d\t%d\t%d\n%d\t%d\t%d\t%d" %(format_number(n)))


