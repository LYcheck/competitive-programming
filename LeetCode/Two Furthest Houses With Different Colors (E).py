class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        sofar = -float('inf')
        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j]:
                    sofar = max(sofar, j-i)
                    
        return sofar