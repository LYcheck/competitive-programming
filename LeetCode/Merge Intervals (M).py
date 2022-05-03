class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:            
        intervals.sort()
        
        res = []
        for interval in intervals:
            if not res: 
                res += [interval]
                continue
            cur = res[-1]
            
            if cur[0] == interval[0]: res[-1][1] = max(cur[1], interval[1])
            elif interval[0] <= cur[1]: res[-1][1] = max(cur[1], interval[1])
            else: res += [interval]
        
        return res