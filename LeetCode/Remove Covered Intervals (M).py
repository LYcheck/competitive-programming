class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def comparator(n1, n2):
            if n1[0] < n2[0]: return -1
            elif n1[0] == n2[0]:
                return -1 if n1[1] > n2[1] else 0
            else:
                return 1

        intervals.sort(key=cmp_to_key(comparator))
        print(intervals)
        
        res = 1
        a, b = intervals[0][0], intervals[0][1]
        
        for interval in intervals:
            if a <= interval[0] and b >= interval[1]:
                continue
            else:
                a = interval[0]
                b = interval[1]
                res += 1
            
        return res