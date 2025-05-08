class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        start = prices[0]
        end = 0
        max_profit = 0
        for i in range(1,n):
            if prices[i]<start:
                max_profit = max(max_profit,end-start)
                start = prices[i]
                end = 0
            end = max(end,prices[i])
        return max(max_profit,end-start)
            


        