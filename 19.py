'''
对于一个有向图，请实现一个算法，找出两点之间是否存在一条路径。
给定图中的两个结点的指针UndirectedGraphNode* a,UndirectedGraphNode* b(请不要在意数据类型，图是有向图),请返回一个bool，代表两点之间是否存在一条路径(a到b或b到a)。
'''
# -*- coding:utf-8 -*-
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
class Path:
    def checkPath(self, a, b):
        # write code here
        if self.check(a,b):
            return True
        self.m={}
        if self.check(b,a):
            return True
        return False

    def __init__(self):
        self.m = {}

    def check(self,a,b):
        if a.label==b.label:
            return True
        self.m[a]=True
        if(len(a.neighbors)>0):
            for i in a.neighbors:
               if i not in self.m and self.check(i,b):
                   return True
        return False