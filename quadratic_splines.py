# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:12:50 2018

@author: RenTeng
"""

import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#二次样条法


#原函数
def func(x):
    fx = 0.2*x**6-0.2*x**5+0.75*x**3+0.25*x**3-1.75*x**2+1.25*x+5
    return fx

#拟合函数
def nfuc(x,a,b,c):
    fx = a*x**2+b*x+c
    return fx
#拟合函数阶数
n = 6

#随机生成函数坐标
x = [3,4.5,7,9]
y = [2.5,1,2.5,0.5]
#x = []
#y = []
#while len(x)!=n+1:
#    x.append(random.randint(0,20))
#    x = list(set(x))
#for i in x:
#    y.append(func(i))
    
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

#求矩阵
size = (len(x)-1)
gam = np.zeros([3*size,3*size])
l = 0
k = 0
for i in range(0,2*size):
    gam[i][l] = x[k]**2
    gam[i][l+1] = x[k]
    gam[i][l+2] = 1
    if i%2!=0:
        l = l+3
    if i%2!=1 or i==0:
        k+=1
l = 0
k = 1
for i in range(2*size,3*size-1):
    gam[i][l] = x[k]*2
    gam[i][l+1] = 1
    gam[i][l+3] = -x[k]*2
    gam[i][l+4] = -1
  
    l = l+3
    if i%2!=1 or i==0:
        k+=1
gam = gam[0:3*size-1,1:3*size]


yy = []
for i in range(0,len(y)):
    if i!=0 and i!=len(y)-1:
        yy.append(y[i])
        yy.append(y[i])
    else:
        yy.append(y[i])
for i in range(0,len(y)-2):
    yy.append(0)

res = np.linalg.solve(gam,yy)
r = [0]
for i in res:
    r.append(i)

#画拟合函数
plt.style.use('fivethirtyeight')
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(num=1) 
k = 0
for i in range(0,len(x)-1):
    xr = np.arange(x[i],x[i+1],0.05)
    yr = []
    for j in xr:
        yr.append(nfuc(j,r[k],r[k+1],r[k+2]))
    plt.plot(xr,yr)
    plt.scatter(x[i],y[i],100)
    k = k+3
    
plt.scatter(x[i+1],y[i+1],100)


plt.title("拟合函数")
plt.show()
print("1607094245 任腾")