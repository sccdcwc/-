#题目描述
#编写代码，以给定值x为基准将链表分割成两部分，所有小于x的结点排在大于或等于x的结点之前
#给定一个链表的头指针 ListNode* pHead，请返回重新排列后的链表的头指针。注意：分割以后保持原来的数据顺序不变。

# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Partition:
    def partition(self, pHead, x):
        # write code here
        small=ListNode(None)
        sTemp=small
        big=ListNode(None)
        bTemp=big
        pTemp=pHead
        while(pHead!=None):
            if(pHead.val<x):
                if(small.val==None):
                    small=pHead
                    sTemp=small
                else:
                    sTemp.next=pHead
                    sTemp=sTemp.next
            else:
                if(big.val==None):
                    big=pHead
                    bTemp=big
                else:
                    bTemp.next=pHead
                    bTemp=bTemp.next
            pHead=pHead.next
        sTemp.next=None
        bTemp.next=None
        if sTemp.val!=None:
            if bTemp.val!=None:
                sTemp.next=big
        elif(sTemp.val==None):
            small=big
        return small


    def partition2(self, pHead, x):
        small=pHead
        big=pHead
        while pHead!=None:
            if(pHead.val<x):
                small=pHead
            else:
                big=pHead

def addNode(head,x):
    a=ListNode(x)
    head.next=a
    return a

if __name__=="__main__":
    head = ListNode(0)
    temp = head
    sl = [6,2,8,1,3,4,5,7,9,10,2]
    for i in sl:
        head = addNode(head, i)
    p =Partition()
    head=p.partition(temp.next,9)
    while(head.next!=None):
        print(head.val)
        head=head.next
    print(head.val)