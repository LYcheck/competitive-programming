class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stk = []
        
        for i in range(len(heights)-1, -1, -1):
            cur = heights[i]
            if not stk or heights[stk[-1]] < cur:
                stk += [i]
                
        return stk[::-1]