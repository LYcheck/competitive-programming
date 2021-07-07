class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = dict()
        
        for x in s:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        
        for y in t:
            if y not in freq:
                return False
            else:
                freq[y] -= 1
                if freq[y] < 0:
                    return False
        
        return True
