class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        i,j = 0,1
        while j < len(prices):
            maxPro = max(maxPro, prices[j]-prices[i])  
            if prices[i] > prices[j]:
                i = j
            j += 1
        return maxPro
