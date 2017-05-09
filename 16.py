'''题目描述
请编写一个程序，按升序对栈进行排序（即最大元素位于栈顶），要求最多只能使用一个额外的栈存放临时数据，但不得将元素复制到别的数据结构中。
给定一个int[] numbers(C++中为vector&ltint>)，其中第一个元素为栈顶，请返回排序后的栈。请注意这是一个栈，意味着排序过程中你只能访问到第一个元素。
测试样例：
[1,2,3,4,5]
返回：[5,4,3,2,1]'''

# -*- coding:utf-8 -*-
class TwoStacks:
    def twoStacksSort(self, numbers):
        # write code here
        temp=[]
        flag=numbers.pop()
        while(numbers):
            count=0
            b = numbers.pop()
            if(flag<=b):
                if(len(temp)>0):
                    a=temp.pop()
                    while b>a:
                        if(len(temp)>0):
                            numbers.append(a)
                            a=temp.pop()
                            count+=1
                        else:
                            break
                    if (a <= b):
                        temp.append(b)
                        temp.append(a)
                    else:
                        temp.append(a)
                        temp.append(b)
                    for i in range(count):
                        a=numbers.pop()
                        temp.append(a)

                else:
                    temp.append(b)
            else:
                temp.append(flag)
                flag=b
        temp.append(flag)
        return temp
a=[1,2,3,7,5,6,4,8]
s=TwoStacks()
print(s.twoStacksSort(a))
