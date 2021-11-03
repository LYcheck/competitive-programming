class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        n = len(events)
        dp = [0]*n
        vals = [0]*n
        
        vals[n-1] = events[n-1][2]
        
        for i in range(n-2, -1, -1):
            vals[i] = max(events[i][2], vals[i+1])
            
            
        def binsearch(idx):
            l, r = 0, n-1
            res = -1
            
            while l <= r:
                m = (l+r) // 2
                
                if events[m][0] > idx:
                    res = m
                    r = m-1
                else:
                    l = m+1
            return res
        
        resu = 0
        dp[0] = events[0][2]
        
        for i in range(n):
            place = binsearch(events[i][1])
            # print(place)
            if place != -1:
                resu = max(resu, events[i][2]+vals[place])
            else:
                resu = max(resu, events[i][2])
            
        # print(dp) 
        return resu