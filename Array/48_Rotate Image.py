class Solution(object):
    def rotate(self, matrix):
        n, m = len(matrix), len(matrix[0])
        for i in range(n-1):
            for j in range(i+1,m):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        
