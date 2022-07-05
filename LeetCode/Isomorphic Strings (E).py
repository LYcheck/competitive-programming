class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        have = {}
        mapped = {}
        for i in range(len(s)):
            if s[i] in have:
                if t[i] != have[s[i]]: return False
                
            else:
                if t[i] in mapped: return False
                have[s[i]] = t[i]
                mapped[t[i]] = 1
                
        return True

        #can also init ascii array for O(1) space