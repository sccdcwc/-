# -*- coding:utf-8 -*-
class Clearer:
    def clearZero(self, mat, n):
        x=[]
        y=[]
        for i in range(n):
            for l in range(n):
                if(mat[i][l]==0):
                    x.append(i)
                    y.append(l)
        for i in x:
            mat[i]=[0]* n
        for i in y:
            for l in range(n):
                mat[l][i]=0
        return mat

if __name__== "__main__":
    clear=Clearer()
    mat=[[1,2,3,4],[0,1,2,3],[0,0,1,2],[0,0,3,4]]
    print(clear.clearZero(mat,4))