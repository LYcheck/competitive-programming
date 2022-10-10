class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        abc = "abcdefghijklmnopqrstuvwxyz"
        if not s: return 0
        res = 1
        
        for i in range(len(abc)):
            for j in range(i+1, len(abc)):
                temp = abc[i:j+1]
                if temp in s:
                    res = max(res, len(temp))
                    
        return res