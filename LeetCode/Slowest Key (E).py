class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxs = []
        maxn = -1
        prev = 0
        
        for i in range(len(releaseTimes)):
            cur = releaseTimes[i]
            elapsed = cur-prev
            if elapsed > maxn:
                maxs = [keysPressed[i]]
                maxn = elapsed
            elif elapsed == maxn:
                maxs += [keysPressed[i]]
            
            prev = cur
    
            
        return max(maxs)