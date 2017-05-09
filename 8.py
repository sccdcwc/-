# -*- coding:utf-8 -*-
class ReverseEqual:
    def checkReverseEqual(self, s1, s2):
        # write code here
        if(len(s1)!=len(s2)):
            return False
        count=0
        for i in range(len(s1)):
            if(s1.count(s1[i])==s2.count(s1[i])):
                count+=s1.count(s1[i])
            else:
                return False
        if(count<len(s2)):
            return False
        return True

    def checkReverseEqual1(self, s1, s2):
        # write code here
        return len(s1) == len(s2) and s2 in (s1 + s1)


if __name__ == "__main__":
    s1="abcd"
    s2="bcae"
    a=ReverseEqual()
    print(a.checkReverseEqual(s1,s2))