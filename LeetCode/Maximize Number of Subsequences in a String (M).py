class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        n = len(text)
        first, second = 0, 0
        res = 0
        
        for char in text:
            if char == pattern[1]:
                second += 1
                res += first
            if char == pattern[0]:
                first += 1
            
        return max(res+first, res+second)