class Solution:
    def arrangeCoins(self, n: int) -> int:
#         idx = 1
        
#         while ((idx-1)*(idx)//2) <= n:
#             idx += 1
            
#         return idx-2
    
        
        return int((-1+sqrt(1+8*n))//2)