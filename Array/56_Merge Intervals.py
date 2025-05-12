class Solution(object):
    def merge(self, arr):
        ans = []
        n = len(arr)
        arr.sort()
        ans.append(arr[0])
        for i in range(1,n):
            if arr[i][1]<ans[-1][1]:
                continue
            elif arr[i][0]<=ans[-1][1] and arr[i][1]>=ans[-1][1]:
                ans[-1][1] = arr[i][1]
            else:
                ans.append(arr[i])
        return ans

        