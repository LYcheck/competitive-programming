class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        
        while len(s) >= k:
            res += [s[0:k]]
            s = s[k:]
        if s:
            res += [s]
            
        while len(res[-1]) < k:
            res[-1] += fill
            
        return res