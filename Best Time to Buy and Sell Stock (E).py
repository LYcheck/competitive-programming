class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         max = 0
        
#         for i in range(len(prices)-1):
#             for n in range(i, len(prices)):
#                 if (prices[n] - prices[i] > max):
#                     max = prices[n] - prices[i]
                    
#         return max

        # minuend = max(prices[0], prices[1])
        # subtra = min(prices[0], prices[1])
    
        if not prices or len(prices) == 1:
            return 0;
        
        subtra = prices[0]
        res = 0
        
        for i in range(len(prices)):
            cur = prices[i] - subtra
            
            if prices[i] < subtra:
                subtra = prices[i]
            elif cur > res:
                res = cur
            
        return res
