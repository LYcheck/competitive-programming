class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l = 1
        r = m*n
        
        while l < r:
            mid = (l+r)//2
            ctr = 0
            
            for i in range(1,m+1):
                ctr += min(mid//i, n)
            
            if ctr >= k:
                r = mid
            else:
                l = mid+1
                
        return l
                