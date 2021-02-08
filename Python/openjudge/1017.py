#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:48:08 2020

@author: zuoxichen
"""
def nplus(integer1,integer2):
    a= integer1/integer2 if integer1%integer2==0 else (integer1//integer2)+1
    return int(a)
def thr(integer):
    a=[]
    if integer%4==1:
        a=[20,7]
    elif integer%4==2:
        a=[12,6]
    else:
        a=[4,5]
    return a
a=True
while a==True:
    b=list(int(i) for i in (input().split())) # b[0]-1 b[1]-2 b[2]-3
    if b.count(0)==6:
        break
    else:
        n1=b[5]+b[4]+b[3] # 6*6 5*5 4*4
        l1=int(b[4]*11-b[0])   # if 5*5 can contain 1*1
        l2=int(b[3]*20-b[1]*4) # if 4*4 can contain 2*2
        if b[2]%4==0:     # if 3*3 can use case without space
            n1+=int(b[2]/4) # the number of the cases that 3*3 use
            if l2>=0:
                n1+=0 if l1+l2>=0 else nplus(-l1-l2,36)
            else:
                n1+=nplus(-l2,36)
                if l2%36==0:
                    n1+=0 if l1>=0 else nplus(-l1,36)
                else:
                    n1+=0 if l1+36-(-l2)%36 >=0 else nplus(int(-(l1+36-(-l2)%36)),36)
        else:        # 3*3 take a more box
            list1=thr(b[2])
            n1+=(b[2]//4)+1  # 3*3 box
            if l2>0:  
                n1+= 0 if l1+l2+sum(list1)>=0 else nplus(-(l1+l2+sum(list1)),36)
            else:  # 4*4 can not contain 2*2
                l3=list1[0]+l2  # 3*3 can contian 2*2 
                if l3>0:
                   n1+=0 if list1[1]+l3+l1>=0 else nplus(-(list1[1]+l1+l3),36)
                else: # 3*3 cannot contain 2*2 
                    n1+=nplus(-l3,36)
                    if l3%36==0:
                        n1+=0 if list1[1]+l1>=0 else nplus(-(l1+list1[1]),36)
                    else:
                        n1+=0 if list1[1]+l1+36-(-l3)%36>=0 else nplus(int(-(list1[1]+l1+36-(-l3)%36)),36)
    print(n1)