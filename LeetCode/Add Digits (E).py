class Solution:
    def addDigits(self, num: int) -> int:
        
        return 1 + (num-1) % (10-1) if num else 0
        
        if not num: return 0
        
        while len(str(num)) != 1:
            res = 0
            for x in str(num):
                res += int(x)
            num = res
            
        return num