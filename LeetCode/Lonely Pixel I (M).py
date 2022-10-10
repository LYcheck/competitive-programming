class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows, cols = len(picture), len(picture[0])
        
        rcand = [None]*rows
        ccand = [None]*cols
        
        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == 'B':
                    if rcand[r] != None:
                        rcand[r] = None
                        break
                    else: rcand[r] = c
                        
        for c in range(cols):
            for r in range(rows):
                if picture[r][c] == 'B':
                    if ccand[c] != None:
                        ccand[c] = None
                        break
                    else: ccand[c] = r
        
        if rows > cols:
            rcand, ccand == ccand, rcand
            
        res = 0               
        for i in range(rows):
            if rcand[i] != None: res += ccand[rcand[i]] == i
        return res