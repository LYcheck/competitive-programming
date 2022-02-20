class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        q = []
        chars = {}
        
        for _ in s1:
            if _ in chars: chars[_] += 1
            else: chars[_] = 1
            
        idx = 0
        count = n1
        while idx < n2 and count > 0:
            cur = s2[idx]
            
            if cur in chars:
                if chars[cur] > 0: count -= 1
                chars[cur] -= 1
            
            q += [cur]
            idx += 1
            
            if idx <= n1: continue
                
            toPop = q[0]
            q.pop(0)
            
            if toPop in chars:
                if chars[toPop] >= 0: count += 1
                chars[toPop] += 1
        
        return count == 0