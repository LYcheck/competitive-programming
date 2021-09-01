class Solution:
    def numTrees(self, n: int) -> int:
        prod = 1
        for _ in range(2,n+1):
            prod *= (n+_)/_
            
        return round(prod)