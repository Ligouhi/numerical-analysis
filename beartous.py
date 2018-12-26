# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 19:50:52 2018

@author: RenTeng
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

#损失计算
def loss(new,old):
    rate = abs(new-old)/abs(new)
    return rate
#所求函数
def func(x):
    fx = x**5-3.5*x**4+2.75*x**3+2.125*x**2-3.875*x+1.25
    return fx
#求b,c迭代过程
def itr(a,r,s):
    n = len(a)
    b0 = a[0]
    b1 = a[1]+r*b0
    res = []
    res.append(b0)
    res.append(b1)
    for i in range(2,n):
        b2 = a[i]+r*b1+s*b0
        b0 = b1
        b1 = b2
        res.append(b2)
    return res
#一次方程求解
def slove(x,y):
 
    return np.linalg.solve(x,y)


a = [1,-3.5,2.75,2.125,-3.875,1.25]
r = -1
s = -1
pr = r*2
ps = s*2
i = 0
mi = 5
res = []

def bearstou(a,r,s,mi): #（系数数组，r，s初值，当前阶数）
    b = itr(a,r,s)
    c = itr(b,r,s)
    n = len(b)-1
    pr = r
    ps = s
    dr,ds = slove([[c[n-1],c[n-2]],[c[n-2],c[n-3]]],[b[n],b[n-1]])
    r = r-dr
    s = s-ds
    if loss(r,pr)<0.01 and loss(s,ps)<0.01:  
        mi = mi-2
        if(r**2+4*s>0):
                res.append((r+math.sqrt(r**2+4*s))/2)
                res.append((r-math.sqrt(r**2+4*s))/2)
        else:
            res.append(str(r/2)+'+'+str(math.sqrt(abs(r**2+4*s))/2)+'i')
            res.append(str(r/2)+'-'+str(math.sqrt(abs(r**2+4*s))/2)+'i')
        if mi>2: 
            la = [] 
            mi = -1
            for i in b:
                if abs(i)>0.1:
                    mi+=1
                    la.append(i)
            bearstou(la,r,s,mi)
        elif mi == 2:
            if(r**2+4*s>0):
                res.append((r+math.sqrt(r**2+4*s))/2)
                res.append((r-math.sqrt(r**2+4*s))/2)
            else:
                 res.append(str(r/2)+'+'+str(math.sqrt(abs(r**2+4*s))/2)+'i')
                 res.append(str(r/2)+'-'+str(math.sqrt(abs(r**2+4*s))/2)+'i')
        elif mi == 1:
                x = -s/r
                res.append(x)    
    else:
        bearstou(a,r,s,mi)
bearstou(a,r,s,mi)

#画函数图
plt.style.use('fivethirtyeight')
fig = plt.figure(num=1) 
xr = np.arange(-1.5,3,0.1)
yr = []
for i in xr:
    yr.append(func(i))
fig = plt.figure(num=1)
plt.plot(xr,yr)
plt.plot(xr,np.zeros(len(xr)))
plt.show()

#fig = plt.figure(num=1) 
#ax = fig.gca(projection='3d')
#xr = np.arange(-1.4,3,0.1)
#yr = []
#for i in xr:
#    yr.append(func(i))
#z = np.array(yr)
#ax.plot(xr, np.zeros(len(xr)),z )
#ax.plot(np.zeros(len(xr)),xr, z)
#plt.title("function plot")
#plt.show()
print("函数的解有:" )
for i in res:
    print(i)