class Solution(object):
    def recursion(self,index,arr,target,n,curr,result):
        if target==0:
            result.append(list(curr))
            return
        if index>=n or target<0:
            return
        for i in range(index,n):
            if i>index and arr[i]==arr[i-1]:
                continue
            curr.append(arr[i])
            self.recursion(i+1,arr,target-arr[i],n,curr,result)
            curr.pop()
        

    def combinationSum2(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        index = 0
        curr = []
        result = []
        self.recursion(index,candidates,target,n,curr,result)
        return result
        