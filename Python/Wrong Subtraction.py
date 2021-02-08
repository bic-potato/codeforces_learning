#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:03:17 2020

@author: zuoxichen
"""
def string_to_list(string):
    list1=list()
    for i in string:
        list1.extend(i)
    return list1
def init ():
    a=input()
    list2=list(a.split(" "))
    return list2
def divid_string(list):
    a=str(list[0])
    return a
def main_args ():
    list1=init()
    num=int(divid_string(list1))
    k=int(list1[1])
    i=0
    while (i<k):
        list3=string_to_list(str(int(num)))
        if(int(list3[-1])!=0):
            num-=1
        else:
            num/=10
            '''
             除法返回结果保留小数点
            '''
        i+=1
    else:
        return int(num)
print(main_args())