class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        
        left = right = res = 0
        sub = ""
        
        while right < length:
            if s[right] not in sub:
                sub += s[right]
                right += 1
            else:
                left += 1
                sub = sub[1:]
            if right-left > res:
                res = right-left
        
        return res
