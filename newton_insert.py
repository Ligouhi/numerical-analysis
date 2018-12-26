# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:19:19 2018

@author: RenTeng
"""
import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#原函数
def func(x):
    fx = x**5-3.5*x**4+2.75*x**3+2.125*x**2-3.875*x+1.25
    return fx

#拟合函数阶数
n = 4

#随机生成函数坐标
x = []
y = []
while len(x)!=n+1:
    x.append(random.randint(0,20))
    x = list(set(x))
for i in x:
    y.append(func(i))


#x = [1,4,6,5]
#y =[0,1.3863,1.7918,1.6094]
#画函数图
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
plt.title("原函数-5阶及所选坐标")
plt.show()

#求b值
print("1607094245 任腾")
p = int(input("输入要求的x值:"))
b = []

def newton(x,y,n):
    if(len(y)==1):
        b.append(y[0])
        return
    b.append(y[0])
    tmp = []
    for i in range(0,len(x)-n):
        tmp.append((y[i+1]-y[i])/(x[n+i]-x[i]))
    y = tmp
    n+=1
    newton(x,y,n)
newton(x,y,1)

#计算y值
def nihe_func(xx,n):
    if(n==0):
        return b[0]
    fx = b[n]
    for i in range(0,n):
        fx = fx*(xx-x[i])
    n = n-1
    return fx+nihe_func(xx,n)

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
    yr.append(nihe_func(i,n))
plt.plot(xr,yr)
plt.title("原函数-5阶及拟合函数")
plt.show()


real = func(p)
nihe = nihe_func(p,n)
if real == 0:
    print("真实值为:",real," 测试值为:",nihe," 误差为:",abs(real-nihe))
else:
    print("真实值为:",real," 测试值为:",nihe," 误差为:",abs(real-nihe)/abs(real))

