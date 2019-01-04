# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 11:00:53 2019

@author: RenTeng
"""
import matplotlib.pyplot as plt
import numpy as np
import sympy

def func(x):
    fx = -0.5*x**4+4*x**3-10*x**2+8.5*x+1
    return fx
def func_deri(x0):
    x = sympy.Symbol("x")
    a = sympy.diff(-0.5*x**4+4*x**3-10*x**2+8.5*x+1,x)
    return a.evalf(subs = {x:x0})

#画函数图
xs = np.arange(0,4,0.1)
y = []
for i in xs:
    y.append(func(i))
fig = plt.figure(num=1)
plt.plot(xs,y)
plt.title("function plot")
plt.show()

x0 = float(input("input initialize x:"))
d = float(input("input step length:"))

y_pre = []
x_pre = []
tmp = x0
x_pre.append(tmp)
y_pre.append(func(tmp))
lens = int(4/d)
for i in range(0,lens): 
    
    k = (func_deri(tmp)+func_deri(tmp+d))/2
    y_pre.append(y_pre[i]+k*d)
    print(k*d,func(tmp+d))
    tmp+=d
    x_pre.append(tmp)
#画预测函数图
xs = np.arange(x0,x0+4,0.1)
y = []
for i in xs:
    y.append(func(i))
plt.plot(xs,y)
plt.plot(x_pre,y_pre)
for i in range(0,len(x_pre)):
    plt.scatter(x_pre,y_pre)

plt.show()