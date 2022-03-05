class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        temp = 26**(n-1)
        for i in range(n):
            res += temp*(ord(columnTitle[i])-64)
            temp //= 26
        
        return res