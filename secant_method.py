# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:08:30 2018

@author: RenTeng
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def loss(new,old):
    rate = abs(new-old)/abs(new)
    return rate

def func(x):
    fx = x**2-2*x
    return fx

#画函数图
x = np.arange(-2,4,0.1)
y = []
for i in x:
    y.append(func(i))
fig = plt.figure(num=1)
plt.plot(x,y)
plt.plot(x,np.zeros(len(x)))
plt.title("function plot")
plt.show()


x0 = float(input("input x0:"))
x1 = float(input("input x1:"))
Range = max(x0,x1)
x2 = x1-(func(x1)*(x0-x1))/(func(x0)-func(x1))
c = 0
x = []
y = []
x.append(x1)
y.append(func(x1))

x.append(x2)
y.append(0)
while loss(x2,x1)>0.0001:
    preloss = loss(x2,x1)
    x0 = x1
    x1 = x2
    x2 = x1-(func(x1)*(x0-x1))/(func(x0)-func(x1))
    if(preloss<loss(x1,x0) and c>1):
        print("Function does not converge！")
        break
    x.append(x1)
    y.append(func(x1))
    x.append(x2)
    y.append(0)
    c+=1


#画函数图 
xr = np.arange(-2,Range+1,0.1)
yr = []
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