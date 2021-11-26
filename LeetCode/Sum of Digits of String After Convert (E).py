class Solution:
    def getLucky(self, s: str, k: int) -> int:
        charsum = 0
        res = 0
        for char in s:
            if ord(char)-96 > 9:
                res *= 100
            else:
                res *= 10
            res += ord(char)-96
        
        for i in range(k):
            charsum = 0
            while res != 0:
                charsum += res%10
                res = res // 10
            res = charsum
            
        return res