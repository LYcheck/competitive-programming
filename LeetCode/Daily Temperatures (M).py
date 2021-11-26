class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        times = [0]*n
        stk = []
        
        for i in range(n-1, -1, -1):
            while len(stk) > 0 and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
                
            if not stk:
                times[i] = 0
            else:
                times[i] = stk[-1]-i
                
            stk.append(i)
                    
        return times
    