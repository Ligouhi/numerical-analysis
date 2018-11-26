# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 19:41:37 2018

@author: RenTeng
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def loss(b,c):
    rate = b/c
    return rate

def func(x):
    fx = x**2+2*x-24
    return fx

def bn(a,xk):
    n = len(a)
    b = a[0]
    res = []
    res.append(b)
    for i in range(1,n):
        b1 = a[i]+xk*b
        b = b1
        res.append(b)
    return b,res
a = [1,2,-24]
xk = 4
bf,b = bn(a,xk)
cf,c = bn(b,xk)

res = xk-bf/cf

