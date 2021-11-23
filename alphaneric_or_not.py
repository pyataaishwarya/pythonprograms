#!/bin/python

def alphabet_numeric_special(c):
    if ((c>=97 and c<=122) or (c>=65 and c<=90)):
        return 1
    elif (c>=48 and c<=57):
        return 2
    else:
        return 3
c=eval(input("enter c value"))
c1=alphabet_numeric_special(c)
if (c1==1):
    print(c,"it is alphabet")
elif (c1==2):
    print(c,"it is numeric")
else:
    print(c,"it is special character")


