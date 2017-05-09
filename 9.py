# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if(head!=None):
            list=[]
            while(head.next!=None):
                list.append(head)
                head=head.next
            list.append(head)
            if(k<=0):
                return None
            elif(k<=len(list)):
                return list[len(list)-k]
            else:
                return None
        else:
            return None

    def addNode(self,head,x):
        a=ListNode(x)
        head.next=a
        return a
if __name__ == "__main__":
    head=ListNode(0)
    temp=head
    sl=Solution()
    for i in range(1,5):
        head=sl.addNode(head,i)
    print(head.val)
    print(temp.val)
