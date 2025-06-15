class Solution(object):
    def recursion(self,index,nums,ans):
        if index == len(nums):
            ans.append(nums[:])
            return
        for i in range(index,len(nums)):
            nums[i],nums[index]=nums[index],nums[i]
            self.recursion(index+1,nums,ans)
            nums[i],nums[index]=nums[index],nums[i]
    def permute(self, nums):
        ans = []
        index = 0
        self.recursion(index,nums,ans)
        return ans