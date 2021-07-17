class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        exp = abs(n)
        res = 1
        
        while exp > 0:
            if exp & 1:
                res *= x
                
            x *= x
            exp >>= 1
        
        if n > 0:
            return res
        else:
            return 1/res
