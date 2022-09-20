class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        have = {}
        
        for i, _ in enumerate(s):
            if _ in have: have[_] += [i]
            else: have[_] = [i]
        
        for k in have.keys():
            cur = ord(k) - ord('a')
            x, y = have[k][0], have[k][1]
            
            if y-x-1 != distance[cur]: return False
            
        return True