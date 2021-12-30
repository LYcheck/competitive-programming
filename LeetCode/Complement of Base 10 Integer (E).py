class Solution:
    def bitwiseComplement(self, n: int) -> int:
        i = 1
        
        if n == 0:
            return 1
        
        while i <= n:
            n ^= i
            
            i <<= 1
                
        return n