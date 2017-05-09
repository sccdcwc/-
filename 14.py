'''
请实现一种数据结构SetOfStacks，由多个栈组成，其中每个栈的大小为size，当前一个栈填满时，新建一个栈。该数据结构应支持与普通栈相同的push和pop操作。
给定一个操作序列int[][2] ope(C++为vector<vector<int>>)，每个操作的第一个数代表操作类型，
若为1，则为push操作，后一个数为应push的数字；若为2，则为pop操作，后一个数无意义。
请返回一个int[][](C++为vector<vector<int>>)，为完成所有操作后的SetOfStacks，顺序应为从下到上，
默认初始的SetOfStacks为空。保证数据合法。
'''

# -*- coding:utf-8 -*-
class SetOfStacks:
    def setOfStacks(self, ope, size):
        # write code here
        list=[]
        stack=[]
        l=0
        for i in ope:
            if i[0]==1:
                if l<size-1:
                    list.append(i[1])
                    l+=1
                else:
                    list.append(i[1])
                    stack.append(list)
                    list=[]
                    l=0
            if i[0]==2:
                if l !=0:
                    list.pop()
                    l-=1
                elif l == 0:
                    list=stack.pop()
                    list.pop()
                    l=size-1
        if len(list)!=0:
            stack.append(list)
        return stack

size=2
ope=[[1,97868],[1,69995],[1,28525],[1,72341],[1,86916],[1,5966],[2,58473],[2,93399],[1,84955],[1,16420],[1,96091],[1,45179],[1,59472],[1,49594],[1,67060],[1,25466],[1,50357],[1,83509],[1,39489],[2,51884],[1,34140],[1,8981],[1,50722],[1,65104],[1,61130],[1,92187],[2,2191],[1,2908],[1,63673],[2,92805],[1,29442]]
s=SetOfStacks();
print(s.setOfStacks(ope,size))