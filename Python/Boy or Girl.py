#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:13:42 2020

@author: zuoxichen
"""
def String_to_Set(String):
    set1=set()
    for i in String:
        set1.add(i)
    return set1
def main_approach(set):
    a=len(set)
    if (a%2==0):
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
a=input()
set2= String_to_Set(a)
main_approach(set2)