# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:10:49 2018

@author: RenTeng
"""

import matplotlib.pyplot as plt
import numpy as np

xi = np.array([0,0.2,0.4,0.6,0.8])
yi = np.array([0.9,1.9,2.8,3.3,4.2])

for i in range(0,len(xi)):
    plt.scatter(xi[i],yi[i])

mat1 = np.array([[len(xi),xi.sum()],[xi.sum(),np.sum(np.square(xi))]])
mat2 = np.array([yi.sum(),np.sum(xi*yi)])
a,b = np.linalg.solve(mat1,mat2)
print('function: y = {0:n}+{1:n}x'.format(a,b))

def func(a,b,x):
    fx = a+b*x
    return fx

xr = np.arange(0,1,0.1)
yr = []
for i in xr:
    yr.append(func(a,b,i))

plt.plot(xr,yr)
plt.show()