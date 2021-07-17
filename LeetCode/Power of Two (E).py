class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        check = 1
        
        while n >= check:
            if check == n:
                return 1
            check <<= 1
        
        return 0
