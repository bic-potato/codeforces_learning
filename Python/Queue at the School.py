#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 18:15:49 2020

@author: zuoxichen
"""

def String_to_List ():
    a=input()
    list1=list()
    for i in a:
        list1.append(i)
    return list1

def INIT ():
    a=input()
    list1=a.split(" ")
    return list1

def get_order (list2):
    list1=list()
    i=0
    while "B" in list2:
        b=list2.index("B")
        c=b+i
        list1.append(c)
        list2.remove("B")
        i+=1
    else:
        return list1

def reconstructure (num1,num2,list2):
    list1=list()
    for i in list2:
        a=int(i)
        a+=num1
        if (a>num2):
            a=num2
        while a in list1:
            a-=1
        else:
            list1.append(a)  
    return list1

def get_NewList (num,list2):
    i=0
    list1=list()
    while (i<num):
        if i in list2:
            list1.append("B")
        else:
            list1.append('G')
        i+=1
    else:
        for i in list1:
            print(i,end="")
         
    
def main_args():
    list1=INIT()
    list2=String_to_List()
    list3=get_order(list2)
    n=int(list1[0])
    t=int(list1[1])
    list4=reconstructure(t,n,list3)
    get_NewList(n, list4)    


main_args()
    
    
    
    
    
    
    
    
    