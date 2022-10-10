class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        uniqs = 0
        have = {}
        n = len(s)
        l, r = 0, 0
        res = 0
        
        while r < n:
            if s[r] not in have:
                uniqs += 1
                have[s[r]] = 1
            else:
                have[s[r]] += 1
            
            while uniqs > 2:
                have[s[l]] -= 1
                if have[s[l]] == 0:
                    del have[s[l]]
                    uniqs-=1
                l += 1
            
            r += 1
            res = max(res, r-l) 
        
        return res