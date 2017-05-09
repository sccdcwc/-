#有两个用链表表示的整数，每个结点包含一个数位。这些数位是反向存放的，也就是个位排在链表的首部。编写函数对这两个整数求和，并用链表形式返回结果。
#给定两个链表ListNode* A，ListNode* B，请返回A+B的结果(ListNode*)。

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
      self.val = x
      self.next = None
class Plus:
    def plusABforvalue(self, a, b):
        # write code here
        lista=[]
        listb=[]
        count=0
        while a is not None:
            lista.append(a.val)
            a=a.next
        while b is not None:
            listb.append(b.val)
            b= b.next
        lena=len(lista)
        lenb=len(listb)
        if lena>lenb:
            while len(listb)!=lena:
                listb.append(0)
        else:
            while len(lista) != lenb:
                lista.append(0)
        for i in range(len(lista)):
            count += (lista[i] + listb[i]) * (10 ** i)
        return count

    def plusAB(self, a, b):
        flag=0
        c=ListNode(0)
        chead=c
        while a is not None and b is not None:
            if a.val+b.val<10:
                if flag == 0:
                    temp = ListNode(a.val+b.val)
                    c.next = temp
                    c = c.next
                    flag=0
                else:
                    if(a.val+b.val+1<10):
                        temp = ListNode(a.val+b.val+1)
                    else:
                        temp=ListNode(0)
                        flag=1
                    c.next = temp
                    c = c.next
            else:
                if flag==0:
                    temp=ListNode((a.val+b.val)%10)
                    c.next=temp
                    c=c.next
                    flag=1
                else:
                    temp = ListNode((a.val + b.val+1) % 10)
                    c.next = temp
                    flag = 1
                    c = c.next

        while a is not None:
            if(flag==1):
                if(a.val+1==10):
                    flag=1
                    temp=ListNode(0)
                else:
                    flag=0
                    temp=ListNode(a.val+1)
                c.next=temp
                c=c.next

        while b is not None:
            if(flag==1):
                if(b.val+1==10):
                    flag=1
                    temp=ListNode(0)
                else:
                    flag=0
                    temp=ListNode(b.val+1)
                c.next=temp
                c=c.next
        return chead

    def plusAB1(self, a, b):
        flag=0
        c=ListNode(0)
        chead=c
        while a is not None and b is not None:
            if a.val+b.val<10:
                if flag == 0:
                    temp = ListNode(a.val+b.val)
                    c.next = temp
                    c = c.next
                    flag=0
                else:
                    if(a.val+b.val+1<10):
                        temp = ListNode(a.val+b.val+1)
                    else:
                        temp=ListNode(0)
                        flag=1
                    c.next = temp
                    c = c.next
            else:
                if flag==0:
                    temp=ListNode((a.val+b.val)%10)
                    c.next=temp
                    c=c.next
                    flag=1
                else:
                    temp = ListNode((a.val + b.val+1) % 10)
                    c.next = temp
                    flag = 1
                    c = c.next

        while a is not None:
            if(flag==1):
                if(a.val+1==10):
                    flag=1
                    temp=ListNode(0)
                else:
                    flag=0
                    temp=ListNode(a.val+1)
                c.next=temp
                c=c.next

        while b is not None:
            if(flag==1):
                if(b.val+1==10):
                    flag=1
                    temp=ListNode(0)
                else:
                    flag=0
                    temp=ListNode(b.val+1)
                c.next=temp
                c=c.next
        return chead

def addNode(head,x):
    a=ListNode(x)
    head.next=a
    return a

if __name__=="__main__":
    head1 = ListNode(0)
    head2 = ListNode(0)
    temp1 = head1
    temp2=head2
    s1 = [3,2,1]
    s2 = [1,2,3]
    for i in s1:
        head1 = addNode(head1, i)
    for i in s2:
        head2=addNode(head2,i)
    p=Plus()
    print(p.plusAB(temp1.next,temp2.next))
