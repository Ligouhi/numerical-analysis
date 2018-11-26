# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:10:24 2018

@author: RenTeng
"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def loss(new,old):
    rate = abs(new-old)/abs(new)
    return rate

import sympy

def func(x):
    fx = x**2-2*x
    return fx
def func_deri(x):
    x0 = sympy.Symbol("x")
    a = sympy.diff(x0**2-2*x0,x0)
    return a.evalf(subs = {x0:x})

#画函数图
xs = np.arange(-2,4,0.1)
y = []
for i in xs:
    y.append(func(i))
fig = plt.figure(num=1)
plt.plot(xs,y)
plt.plot(xs,np.zeros(len(xs)))
plt.title("function plot")
plt.show()


x0 = float(input("input initialize x:"))
x1 = x0-func(x0)/func_deri(x0)
Range = x0
c = 0
x = []
y = []
x.append(x0)
y.append(func(x0))
x.append(x1)
y.append(0)

#迭代过程
while loss(x1,x0)>0.0001:
    preloss = loss(x1,x0)
    x0 = x1
   
    x1 = x0-func(x0)/func_deri(x0)
    x.append(x0)
    y.append(func(x0))
    x.append(x1)
    y.append(0)

    if(preloss<loss(x1,x0) and c>1):
        print("Function does not converge！")
        break
    c+=1


#描点 
xr = np.arange(-2,Range+1,0.1)
yr = []
plt.plot(xr,np.zeros(len(xr)))
for i in xr:
    yr.append(func(i))
fig = plt.figure(num=1)
plt.plot(xr,yr)
plt.ion()
for i in range(0,len(x)-1):
    plt.scatter(x[i],y[i])
    plt.plot((x[i],x[i+1]),(y[i],y[i+1]))

#    plt.pause(0.5)
plt.grid()
plt.show()




print("Approximate solution:",x1)