#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.list1=[]
        self.list2=[]
    def push(self, node):
        # write code here
        self.list1.append(node)
    def pop(self):
        # return xx
        if(len(self.list2)==0):
            l=len(self.list1)
            for i in range(l):
                self.list2.append(self.list1.pop())
        return self.list2.pop()


s=Solution()
s.push(1)
s.push(2)
print(s.pop())
s.push(3)
print(s.pop())

