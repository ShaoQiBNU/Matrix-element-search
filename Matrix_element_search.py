class Finder:
    def findElement(self, mat, n, m, x):

        i=0
        j=m-1

        while i<n and j>=0:

            if mat[i][j]==x:
                return [i,j]

            ## 列减1
            elif mat[i][j]>x:
                j=j-1

            ## 行+1
            else:
                i=i+1

if __name__ == '__main__':
    
    mat=[[1,2,3],[4,5,6]]
    
    f=Finder()
    print(f.findElement(mat,2,3,6))
