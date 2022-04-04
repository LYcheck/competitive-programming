class Solution:
    def brokenCalc(self, y: int, x: int) -> int:
        res = 0
        
        while x > y:
            if x & 1: x += 1
            else: x //=2
            res += 1
        
        if x < y: res += y-x
        return res