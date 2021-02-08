#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:15:10 2020

@author: zuoxichen
"""
def input_int():
     a=int(input())
     return a
 
k=input_int()
l=input_int()
m=input_int()
n=input_int()
d=input_int()
q=0
for i in range(1,d+1):
    if i%k==0 or i%m==0 or i%l==0 or i%n==0:
        q+=1
print(q)