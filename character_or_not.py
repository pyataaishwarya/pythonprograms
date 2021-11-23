#!/bin/python

def character_or_not(c):
    if ((c>=97 and c<=122)or (c>=65 and c<=90)):
        return 1
    return 0
c=int(input("enter the number"))
if(character_or_not(c)==1):
    print("it is a alphabet")
else:
    print("it is not a alphbet")

