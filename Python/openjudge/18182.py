#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:09:01 2020

@author: zuoxichen
"""
def DamageData(dictionary,list1):
    if list1[0] in dictionary:
        if type(dictionary[list1[0]])==list:
            dictionary[list1[0]].append(list1[1])
        else:
            dictionary[list1[0]]=[list1[1]]
    else:
        dictionary[list1[0]]=[list1[1]]
    return dictionary
     
def main_args(data):
    j=0
    n=data[0] # number of the skill
    m=data[1] # maxmimum number of the skill that can use in one time
    b=data[2] # HP of the monster
    dic1=dict()
    while j<n:
        j+=1
        SkillData=list(int(i) for i in input().split())
        dic1=DamageData(dic1, SkillData)
    else:
        hp=b
        list3=sorted(list(dic1.keys()))
        for i in list3:
            q=0
            list1=dic1[i]
            list2=[]
            while q<m and len(list1)>0:
                q+=1
                list2.append(max(list1))
                list1.remove(max(list1))
            hp-=sum(list2)
            if hp<=0:
                return(i)
        else:
            return('alive')
                    
case=int(input())
i=0
while i<case:
    data=list(int(i) for i in input().split())
    i+=1
    print(main_args(data))
        
