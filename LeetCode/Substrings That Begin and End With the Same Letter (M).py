class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        seen = {}
        res = 0
        
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = 1
            else:
                seen[s[i]] += 1
            
            res += seen[s[i]]  

        return res