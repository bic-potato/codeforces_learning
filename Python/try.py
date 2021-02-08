#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:45:50 2020

@author: zuoxichen
"""
def remove_object(list1,*var1):
    for i in var1:
        if i in list1:
            list1.remove(i)
    return list1

def lower_all(list1):
    list2=[]
    for i in list1:
        i.lower()
        list2.append(i)
    return list2

def print_list(list1):
    for i in list1:
        print(i,end='')

def main_args(list1):
    list2=lower_all(list1)
    list3=remove_object(list2,'a','e','i','o','u')
    n=len(list3)
    i=0
    list4=[]
    while i<2*n:
        if i%2==0:
            list4.append('.')
        else:
            list4.append(list3[int(i/2)])
        i+=1
    print_list(list4)
    return

a=input()
b=list(a)
print(b)
main_args(b)
