class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,1
        maxP = 0
        while j<len(prices):
            if prices[i] > prices[j]:
                i = j
            else:
                maxP = max(prices[j]-prices[i],maxP)
            j += 1
        return maxP