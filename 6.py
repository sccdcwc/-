class Transform:
    def transformImage(self, mat, n):
        for i in range(n):
            for l in range(i):
                if(i!=l):
                    temp=mat[i][l]
                    mat[i][l]=mat[l][i]
                    mat[l][i]=temp
        for i in range(n):
            mat[i].reverse()
        return mat


if __name__=="__main__":
    mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    t=Transform()
    print(t.transformImage(mat,4))