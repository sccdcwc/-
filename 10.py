#题目描述
#实现一个算法，删除单向链表中间的某个结点，假定你只能访问该结点。
#给定带删除的节点，请执行删除操作，若该节点为尾节点，返回false，否则返回true

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Remove:
    def removeNode(self, pNode):
        # write code here
        if pNode.next==None:
            return False
        else:
            pNode=pNode.next
        return True