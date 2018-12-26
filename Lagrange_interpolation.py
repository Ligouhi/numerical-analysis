# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 09:42:24 2018

@author: RenTeng
"""

import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#原函数
def func(x):
    fx = 0.2*x**6-0.2*x**5+0.75*x**3+0.25*x**3-1.75*x**2+1.25*x+5
    return fx

#拟合函数阶数
n = 5

#随机生成函数坐标
x = []
y = []
while len(x)!=n+1:
    x.append(random.randint(0,20))
    x = list(set(x))
for i in x:
    y.append(func(i))

#原函数图
plt.style.use('fivethirtyeight')
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(num=1) 
xr = np.arange(0,20,1)
yr = []
for i in xr:
    yr.append(func(i))
plt.plot(xr,yr)
for i in range(0,len(x)-1):
    plt.scatter(x[i],y[i],100)
plt.title("原函数-6阶")
plt.show()


 
def fx(xx,xi):
    a = 1
    t = x.copy()
    xt = t.pop(xi)
    
    for i in t:
        a*=(xx-i)/(xt-i)
    return a*y[xi]

p = int(input("请输入测试点的x值"))
def yy(p):
    res = 0
    for i in range(0,len(x)):
        res+=fx(p,i)
    return res
res = yy(p)    

#画拟合后的图
plt.style.use('fivethirtyeight')
fig = plt.figure(num=1) 
xr = np.arange(0,20,1)
yr = []
for i in xr:
    yr.append(func(i))
plt.plot(xr,yr)
for i in range(0,len(x)-1):
    plt.scatter(x[i],y[i],100)

xr = np.arange(0,20,1)
yr = []
for i in xr:
    yr.append(yy(i))
plt.plot(xr,yr)
plt.title("原函数-6阶及拟合函数")
plt.show()



real = func(p)
nihe = res
if real == 0:
    print("真实值为:",real," 测试值为:",nihe," 误差为:",abs(real-nihe))
else:
    print("真实值为:",real," 测试值为:",nihe," 误差为:",abs(real-nihe)/abs(real))
    
print("1607094245 任腾")