class Solution(object):
    def recursion(self,nums,index,curr,result,n):
        result.append(list(curr))
        for i in range(index,n):
            if i!=index and nums[i]==nums[i-1]:
                continue
            curr.append(nums[i])
            self.recursion(nums,i+1,curr,result,n)
            curr.pop()

    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)
        index = 0
        result = []
        curr = []
        self.recursion(nums,index,curr,result,n)
        return result
        