class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        seen = {}
        for char in s:
            if char in seen: seen[char] += 1
            else: seen[char] = 1
                
        have = list(seen.keys())
        have.sort(reverse=True)
        n = len(have)
        
        idx = 0
        res = ""
        k = repeatLimit
        while idx < n:
            char = have[idx]
            if seen[char] == 0:
                idx += 1
                k = repeatLimit
            elif k > 0:
                res += char
                seen[char] -= 1
                k -= 1
            else:
                nxtidx = idx+1
                while nxtidx < n and seen[have[nxtidx]] == 0:
                    nxtidx += 1
                    
                if nxtidx == n: break
                else:
                    res += have[nxtidx]
                    seen[have[nxtidx]] -= 1
                k = repeatLimit
                    
        return res