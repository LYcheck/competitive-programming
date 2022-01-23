class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ctr = 0
        temp = target
        while temp != 1:
            if maxDoubles == 0:
                ctr += temp-1
                temp = 1
                
            elif temp & 1 == 0:
                temp >>= 1
                ctr += 1
                maxDoubles -= 1
            
            else:
                temp -= 1
                ctr += 1
        
        return ctr