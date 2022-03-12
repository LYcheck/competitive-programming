class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seen = {}
        for i in range(len(t)):
            if t[i] in seen: seen[t[i]] += [i]
            else: seen[t[i]] = [i]
        
        start = 0
        for char in s:
            if char not in seen or not seen[char]: return False
            while seen[char] and seen[char][0] < start: seen[char].pop(0)
            
            if not seen[char]: return False
            
            start = seen[char][0]
            seen[char].pop(0)
            
        return True