class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        start,mid = 0,0
        end = n-1

        while mid<=end:
            if nums[mid]==0:
                nums[start],nums[mid] = nums[mid],nums[start]
                mid+=1
                start+=1
            elif nums[mid]==2:
                nums[mid],nums[end] = nums[end],nums[mid]
                end-=1
            else:
                mid+=1
        return nums
            
        