class Solution(object):
    def generate(self, n):
        arr = [[1],[1,1]]
        if n == 0:
            return []
        elif n==1:
            return [[1]]
        elif n==2:
            return arr
        
        for i in range(2,n):
            new_arr = []
            j = 0
            while j < len(arr[-1])-1:
                new_arr.append(arr[-1][j]+arr[-1][j+1])
                j+=1
            arr.append([1]+new_arr+[1])
        return arr



        