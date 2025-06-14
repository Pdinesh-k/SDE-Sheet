class Solution(object):
    def recursion(self,index,arr,target,n,curr,result):
        if target==0:
            result.append(list(curr))
            return
        if index>=n or target<0:
            return
        curr.append(arr[index])
        self.recursion(index,arr,target-arr[index],n,curr,result)
        curr.pop()
        self.recursion(index+1,arr,target,n,curr,result)
        

    def combinationSum(self, candidates, target):
        n = len(candidates)
        index = 0
        curr = []
        result = []
        self.recursion(index,candidates,target,n,curr,result)
        return result