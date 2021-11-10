class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        
        for i in range(len(prices)-1):
            maxp += max(prices[i+1]-prices[i], 0)
            
        return maxp