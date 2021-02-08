#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:16:22 2020

@author: zuoxichen
"""
import os
def month(string):
    if string[4:6]=='01':
        a=13
        b=int(string[0:4])-1
        c=int(str(b)[0:2])
        d=int(str(b)[2:3]+str(b)[3])
    elif string[4:6]=='02':
        a=14
        b=int(string[0:4])-1
        c=int(str(b)[0:2])
        d=int(str(b)[2:3]+str(b)[3])
    else:
        a=int(string[4:6])
        c=int(string[0:2])
        d=int(string[2:4])
    dic2={'ar':d,'month':a,'ye':c}
    return dic2

n=int(input())
i=0
dic1={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
while i<n:
    j=input()
    if len(j)==8 and int(j)>15821015:
        dic3=month(j)
        m=dic3['month']
        y=dic3['ar']
        c=int(dic3['ye'])
        d1=j[6:7]
        d=int(d1+j[7])
        year=int(j[0:4])
        w=(y+y//4+c//4-2*c+(26*(m+1))//10+d-1)%7
        if 0<=w<=7:
            print(dic1[int(w)])
        else:
            print('')
        i+=1
    else:
        i+=1
        print('',end='/n')
        continue
else:
    os.system('exit')