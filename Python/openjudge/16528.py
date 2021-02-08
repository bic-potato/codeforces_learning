#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:05:59 2020

@author: zuoxichen
"""
def takeFirst(elem):
    return elem[0]

n = int(input())
ans = 0
list1 = []
i = 0
while i < n:
    list1.append(list(map(int, input().split())))
    i+=1
list1.sort(key=takeFirst)
for i in list1:
    if i[0]<0 or i[-1] > 60:
        list1.remove(i)
listFirst=list(set(takeFirst(i) for i in list1))
list2=[]
j = 0
while j<len(listFirst):
    list2.append([])
    j+=1
dic1=dict(zip(listFirst,list2))
for i in range(len(list1)):
    dic1[list1[i][0]].append(list1[i][-1])
judge = True
p = listFirst[0]
while judge == True:
    if p in dic1 and p+1 in listFirst:
        p = min(dic1[p]) if p!=min(dic1[p]) else listFirst[listFirst.index(p)+1]
        ans+=1
    elif dic1[p][0]==dic1[p][-1] or dic1[p-1][1] <=dic1[p][0]:
        ans+=1
        judge = False
    else:
        judge =False
print(ans)

    