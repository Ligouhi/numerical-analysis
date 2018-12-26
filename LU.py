# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 13:42:59 2018

@author: RenTeng
"""


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class LU:
    def __init__(self,x,y):
#        self.x = np.array([[70,1,0],[60,-1,-1],[40,0,1]],dtype=float)
#        self.y = np.array([636,518,307],dtype=float)
        self.x = x
        self.y = y
        self.ori_x = self.x.copy()
        self.ori_y = self.y.copy()
        self.I = []
        self.L = None
        self.U = None
        print("\nx矩阵\n",self.x,"\ny矩阵\n",self.y)
    
    def scale(self):
        k = False
        for i in range(0,self.x.shape[0]):
            m = np.max(self.ori_x[i])
            self.ori_x[i] = self.ori_x[i]/m
            self.ori_y[i] = self.ori_y[i]/m
            if self.ori_x[i][i]<1e-4:
                k = True
        return k
#        print("\n缩放后\nx矩阵\n",self.x,"\ny矩阵\n",self.y)
    
    def slove(self):
        f = False 
        for i in range(0,self.x.shape[0]-1):
            if self.scale():
                index = np.argmax(self.x,axis=0)
                if index[i]>i:
                    tmp = self.x[index[i]].copy()
                    self.x[index[i]] = self.x[i].copy()
                    self.x[i] = tmp.copy()
                    tmp = self.y[index[i]].copy()
                    self.y[index[i]] = self.y[i].copy()
                    self.y[i] = tmp.copy()
                if self.x[i][i]==0:
                    print("换元后矩阵主元仍含0！")
                    f = True
                    break
            for j in range(i+1,self.x.shape[0]):
                rate = self.x[j][i].copy()/self.x[i][i].copy()
                self.I.append(rate)
                for k in range(0,self.x.shape[1]):
                    self.x[j][k] = self.x[j][k].copy()-rate*self.x[i][k].copy()
#                self.y[j] = self.y[j]-rate*self.y[i].copy()
        if not f:
            self.L = np.eye(self.x.shape[0])
            k = 0
            for i in range(1,self.L.shape[0]):
                for j in range(0,i):
                    self.L[i,j] = self.I[k]
                    k+=1
            print('matrix L\n',self.L)
            print('matrix U\n',self.x)
            tmp = np.zeros(self.L.shape[0])
            for i in range(0,self.L.shape[0]):
                s = self.y[i]
                for j in range(0,i):
                    s-=self.L[i][j]*tmp[j]
                tmp[i] = s/self.L[i][i]
            print('matrix y\n',tmp)
           
            res = np.zeros(self.L.shape[0])
            res[-1] = self.x[-1][-1]
            for i in range(self.x.shape[0]-1,-1,-1):
                s = tmp[i]
                for j in range(i+1,self.x.shape[1]):
                    s-=self.x[i][j]*res[j]
                res[i] = s/self.x[i][i]
            print('matrix x\n',res)
        
        

if __name__ == "__main__":
    print("\n1607094245 任腾")
    x = np.array([[2,2,3],[4,7,7],[-2,4,5]],dtype=float)
    y = np.array([3,1,-7],dtype=float)
    lu = LU(x,y)
    lu.slove()
    
    