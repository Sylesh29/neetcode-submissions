class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, p, l, r = 0,0,0,1
        n = len(prices)
        while r < n:
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                maxP = max(maxP,p)
            else:
                l = r
            r += 1
        return maxP 


        