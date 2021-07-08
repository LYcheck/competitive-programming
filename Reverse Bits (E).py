class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i=31
        
        for j in range(32):
            res += (n&1)*(2**i)
            n >>= 1
            i -= 1
            
        return res
