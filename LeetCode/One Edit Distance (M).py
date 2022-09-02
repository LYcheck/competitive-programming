class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t): s, t = t, s
        ns, nt = len(s), len(t)
        if nt-ns > 1: return False
        
        if ns == nt:
            flag = 0
            for i in range(ns):
                if s[i] != t[i]:
                    if flag: return False
                    flag = 1
            return flag
            
        for i in range(ns):
            if s[i] != t[i]:
                if s[i:] == t[i+1:]: return True
                return False
        
        return True