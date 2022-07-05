class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        have = {}
        targ = 1 << k
        cnt = 0
        
        for i in range(len(s)-k+1):
            temp = s[i:i+k]
            if temp not in have:
                have[temp] = 1
                cnt += 1
                
            if cnt == targ: return True
            
        return False