class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = dict()
        
        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]] = -1
            else:
                hm[s[i]] = i
                
        for j in range(len(s)):
            if hm[s[j]] != -1:
                return hm[s[j]]
            
        return -1