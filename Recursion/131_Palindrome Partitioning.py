class Solution(object):
    def palindrome(self,string):
        return string == string[::-1]
    def recursion(self,index,s,n,curr,res):
        if index==n:
            res.append(list(curr))
            return
        for i in range(index,n):
            if self.palindrome(s[index:i+1]):
                curr.append(s[index:i+1])
                self.recursion(i+1,s,n,curr,res)
                curr.pop()
    def partition(self, s):
        res = []
        curr = []
        index = 0
        n = len(s)
        self.recursion(index,s,n,curr,res)
        return res
        