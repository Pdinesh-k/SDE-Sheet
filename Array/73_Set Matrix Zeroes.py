class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        col_0 = -1

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    #mark row as 0
                    matrix[i][0] = 0
                    #mark col as 0
                    if j!=0:
                        matrix[0][j] = 0
                    else:
                        col_0 = 0


        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        
        if matrix[0][0]==0:
            for col in range(m):
                matrix[0][col] = 0

        if col_0==0:
            for row in range(n):
                matrix[row][0] = 0

        return matrix
        

        