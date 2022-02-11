class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        rtol = []
        ltor = 0
        res = 0
        
        for i in range(n-1, -1, -1):
            if height[i] > 0:
                if not rtol or height[i] > height[rtol[-1]]:
                    rtol += [i]
        
        for j in range(n):
            val = height[j]
            ltor = max(ltor, val)
            
            if rtol: 
                if j > rtol[-1]: rtol.pop()
            if rtol: res += min(ltor, height[rtol[-1]])-val
            
        return res
            
            
        # l->r = [1, 3, 7]
        # r->l = []