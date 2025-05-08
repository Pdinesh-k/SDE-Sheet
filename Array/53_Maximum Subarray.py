class Solution(object):
    def maxSubArray(self, arr):
        n = len(arr)
        sum_ = 0
        max_sum = float("-inf")
        for i in range(n):
            sum_+=arr[i]
            max_sum = max(sum_,max_sum)
            if sum_<0:
                sum_ = 0
        return max_sum


