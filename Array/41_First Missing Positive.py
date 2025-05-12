class Solution(object):
    def firstMissingPositive(self, arr):
        n = len(arr)
        i = 0
        
        while i<n:
            correct_index = arr[i]-1
            if 0 < arr[i] <= n and arr[i] != arr[correct_index]:
                arr[i],arr[correct_index] = arr[correct_index],arr[i]
            else:
                i+=1
                
        for i in range(n):
            if i!=arr[i]-1:
                return i+1
        return n+1