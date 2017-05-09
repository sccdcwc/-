'''
请编写一个函数，检查链表是否为回文。
给定一个链表ListNode* pHead，请返回一个bool，代表链表是否为回文。
测试样例：
{1,2,3,2,1}
返回：true
{1,2,3,2,3}
返回：false
'''

# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Palindrome:
    def isPalindrome(self, pHead):
        # write code here
        c=0
        p1=pHead
        p2=pHead
        list=[]
        flag=0
        while(p1!=None):
            c+=1
            p1=p1.next
        if(c%2==1):
            c=c-1
            flag=1
        l=int(c/2)
        for i in range(l):
            list.append(p2.val)
            p2=p2.next
        if flag==1:
            p2=p2.next
        for i in range(l):
            if(list[len(list)-i-1]!=p2.val):
                return False
            p2=p2.next
        return True

def addNode(head,x):
    a=ListNode(x)
    head.next=a
    return a

if __name__=="__main__":
    head1 = ListNode(0)
    temp1 = head1
    s1 = [5,2,2,3,7,0,7,2,1,0,6,1,0,3,3,3,4,3,4,5,5,4,9,0,9,4,0,6,3,2,2,1,6,7,1,8,2,8,0,6,0,0,4,1,8,2,2,8,1,4,0,0,6,0,8,2,8,1,7,6,1,2,2,3,6,0,4,9,0,9,4,5,5,4,3,4,3,3,3,0,1,6,0,1,2,7,0,7,3,2,2,5]
    for i in s1:
        head1 = addNode(head1, i)
    p=Palindrome()
    print(p.isPalindrome(temp1.next))