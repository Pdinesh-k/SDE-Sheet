class Solution(object):
    def findDuplicate(self, nums):
        n = len(nums)
        i=0
        
        while i<n:
            element = nums[i]
            correct_index = nums[i]-1
            if nums[i]!=nums[correct_index]:
                nums[i],nums[correct_index] = nums[correct_index],nums[i]
            else:
                if i!=correct_index:
                    return element
                i+=1
        
        
            
        