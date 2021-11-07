class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = 10**6
        
        def binGood(x):
            cnt = 0
            
            for quant in quantities:
                cnt += ceil(quant/x)   
            
            return cnt <= n
        
        
        while(l < r):
            m = (l+r)//2
            
            if binGood(m):
                r = m
            else:
                l = m+1
                
        return l
                