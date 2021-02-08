#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 22:37:43 2020

@author: zuoxichen
"""
def main_arguments(number):
    i=0
    maxseats=0
    emptyseats=0
    while i<number:
       a=input()
       list1=list()
       list1.extend(a.split(" "))
       ai=int(list1[0])
       bi=int(list1[1])
       ci=ai-bi
       if i!=number-1:           
           if(ci>=0):
               emptyseats+=ci
               maxseats+=0
           elif(emptyseats+ci>0):
               emptyseats+=ci
               maxseats+=0
           else:
               maxseats-=(ci+emptyseats)
               emptyseats=0
       else:
           maxseats+=0
       i+=1
    else:
        return maxseats
n=int(input())
print(main_arguments(n))