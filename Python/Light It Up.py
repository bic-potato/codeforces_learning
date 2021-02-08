#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:38:25 2020

@author: zuoxichen
"""
'''
#def if_even(num):
 #   if num%2==0:
        a=True
  #  else:
   #     a=False
    return a
'''
def get_open_to_close_tick(l1):
    l2=[]
    for i in l1:
        if l1.index(i)%2!=0:
            l2.append(i)
            l2.sort()
    return l2
def sum_on_time(l1):
    dic=dict()
    for i in l1:
        if l1.index(i)%2!=0:
            dic[i]=i-l1[l1.index(i)-1]
    return dic
s1=input()
s2=input()
l1=s1.split()
l2=s2.split()
se1=list(int(i) for i in l1)
l3=list(int(i) for i in l2)
n=se1[0]
M=se1[1]
l3.insert(0, 0)
l3.insert(-1, M)
l3.sort()
print(l3)
l6=sum_on_time(l3)
t0=sum(list(l6.values()))
l5=get_open_to_close_tick(l3)
l7=list(l6.values())
l8=list(l6.keys())
m=max(l7)
i=l8[l7.index(m)]
l4=set(l3)
l4.add(i+1)
l4=list(l4)
print(l4)
tm=sum(sum_on_time(l4))
print(t0,tm)
if ((tm)>(t0)):
    sum0=tm
else:
    sum0+=0
print(sum0)















