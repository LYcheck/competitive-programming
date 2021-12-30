class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k&1 or k%5 == 0: return -1
        
        rem = 0
        
        for n in range(1, k+1):
            rem = (rem*10+1)%k
            
            if rem == 0: return n
        
        return -1