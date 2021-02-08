#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:09:26 2020

@author: zuoxichen
"""
l1=list(int(i) for i in input().split())  # get list that contains coordinates of the houses
print(max(l1)-min(l1))    # the minimum distance
