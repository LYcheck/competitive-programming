class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        res = 0
        target = len(arr)>>1
        
        vals = list(Counter(arr).values())
        vals.sort(reverse=True)
        
        for n in vals:
            res += 1
            target -= n
            
            if target <= 0:
                return res
