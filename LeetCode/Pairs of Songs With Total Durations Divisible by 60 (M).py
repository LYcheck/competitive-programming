class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ctr = 0
        seen = {}
        
        for num in time:
            num %= 60
            
            if num in seen: seen[num] += 1
            else: seen[num] = 1
                
        for i in range(1, 30):
            if i in seen and 60-i in seen:
                ctr += seen[i]*seen[60-i]
        
        if 0 in seen: ctr += math.comb(seen[0], 2)
        if 30 in seen: ctr += math.comb(seen[30], 2)
                
        return ctr