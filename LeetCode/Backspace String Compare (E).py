class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        idxs, idxt = ns-1, nt-1
        
        while idxs > -1 or idxt > -1:
            backs, backt = 0, 0
            while idxs > -1: 
                if s[idxs] == '#':
                    backs += 1
                    idxs -= 1
                elif backs > 0:
                    idxs -= 1
                    backs -=1
                else:
                    break

            while idxt > -1:
                if t[idxt] == '#':
                    backt += 1
                    idxt -= 1
                elif backt > 0:
                    backt -= 1
                    idxt -= 1
                else:
                    break
            
            if idxt > -1 and idxs > -1:
                if s[idxs] == t[idxt]:
                    idxs -= 1
                    idxt -= 1
                else: return False
                
            elif (idxs < 0 and idxt >= 0) or (idxt < 0 and idxs >= 0): return False

        return True
