class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res, k = 0, 1
        
        while k*(k-1) < 2*n:
            if (n-(k*(k-1))/2)%k == 0:
                res += 1
            k += 1
        
        return res
        
#         res=1
#         for a in range(1,n//2+1):
#             disc = 1-4*(-(a**2)+a-2*n)
            
#             if disc >= 0:
#                 k = (-1+sqrt(disc))/2

#             if k >= a and k == int(k):
#                 res += 1
                
#         return res

        