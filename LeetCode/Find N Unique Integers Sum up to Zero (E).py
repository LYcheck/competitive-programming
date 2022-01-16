class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        
        if n & 1:
            res += [0]
            n -= 1
        
        ctr = 1
        for i in range(n//2):
            res += [ctr]
            res += [-ctr]
            ctr += 1
        
        return res