class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        total = 0
        maxn = -float('inf')
        minn = float('inf')
        
        for _ in differences:
            total += _
            maxn = max(maxn, total)
            minn = min(minn, total)
        
        check = maxn
        
        if len(differences) != 1: 
            check = minn - maxn
            
        ans = 0
        
        for i in range(lower, upper+1):
            if lower <= i+minn <= upper and lower <= i+maxn <= upper: ans += 1
        
        return ans