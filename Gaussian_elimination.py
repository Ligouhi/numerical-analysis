# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 13:42:59 2018

@author: RenTeng
"""


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = np.array([[70,1,0],[60,-1,-1],[40,0,1]],dtype=float)
y = np.array([636,518,307],dtype=float)
ori_x = x.copy()
ori_y = y.copy()
print("\nx矩阵\n",x,"\ny矩阵\n",y)


for i in range(0,x.shape[0]):
    m = np.max(x[i])
    x[i] = x[i]/m
    y[i] = y[i]/m
print("\n缩放后\nx矩阵\n",x,"\ny矩阵\n",y)


f = False
    
for i in range(0,x.shape[0]-1):
    index = np.argmax(x,axis=0)
    if index[i]>i:
        tmp = x[index[i]].copy()
        x[index[i]] = x[i].copy()
        x[i] = tmp.copy()
        tmp = y[index[i]].copy()
        y[index[i]] = y[i].copy()
        y[i] = tmp.copy()
    if x[i][i]==0:
        print("换元后矩阵主元仍含0！")
        f = True
        break
    for j in range(i+1,x.shape[0]):
        rate = x[j][i].copy()/x[i][i].copy()
 
        for k in range(0,x.shape[1]):
            x[j][k] = x[j][k].copy()-rate*x[i][k].copy()
        y[j] = y[j]-rate*y[i].copy()
    
if not f:
    res = np.zeros(3)
    res[-1] = x[-1][-1]
    for i in range(x.shape[0]-1,-1,-1):
        s = y[i]
        for j in range(i+1,x.shape[1]):
            s-=x[i][j]*res[j]
        res[i] = s/x[i][i]
    print("\n解向量\n",res)
    real = np.linalg.solve(ori_x,ori_y)
    print("np库函数求解 \n",real)
print("\n1607094245 任腾")
    
    
    
    
    