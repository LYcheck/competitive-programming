class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #BELLMAN-FORD

        dists = [float('inf')] * n
        
        dists[k-1] = 0
        
        for i in range(n):
            for n1, n2, t in times:
                if dists[n2-1] > t + dists[n1-1]:
                    dists[n2-1] = t + dists[n1-1]
                    
        return max(dists) if max(dists) != float('inf') else -1


