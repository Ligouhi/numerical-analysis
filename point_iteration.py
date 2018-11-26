# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:11:47 2018

@author: RenTeng
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def loss(new,old):
    rate = abs(new-old)/abs(new)
    return rate

def func(x):
    fx = math.e**(-x)-x
    return fx

def it_func(x):
    xx = math.pow(math.e,-x)
    return xx

import math


#画函数图
fig = plt.figure(num=1) 
xr = np.arange(-2,4,0.1)
yr = []
for i in xr:
    yr.append(it_func(i))
fig = plt.figure(num=1)
plt.plot(xr,yr)
plt.plot(xr,xr)
plt.show()


x0 = float(input("input initialize x:"))
Range = x0
x1 = it_func(x0)
c = 0
x = []
y = []
x.append(x0)
y.append(x1)
while loss(x1,x0)>0.0001:
    preloss = loss(x1,x0)
    x0 = x1
    x.append(x0)
    y.append(x1)
    x1 = it_func(x0)
    if(preloss<loss(x1,x0) and c>1):
        print("Function does not converge！")
        break
    x.append(x0)
    y.append(x1)
    c+=1
    
#画函数图 
xr = np.arange(-2,Range+1,0.1)
yr = []
for i in xr:
    yr.append(it_func(i))
fig = plt.figure(num=1)
plt.plot(xr,yr)
plt.plot(xr,xr)
plt.ion()
for i in range(0,len(x)-1):
    plt.scatter(x[i],y[i])
    plt.plot((x[i],x[i+1]),(y[i],y[i+1]))
#    plt.pause(0.5)
plt.grid()
plt.show()

print("Approximate solution:",x1)