class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        fromleft = [False]*n
        fromright = [False]*n
        ctr = 1
        res = []
        for i in range(1, n):
            fromleft[i] = ctr >= k
            if nums[i] <= nums[i-1]: ctr += 1
            else: ctr = 1
        
        ctr = 1
        for i in range(n-2, -1, -1):
            fromright[i] = ctr >= k
            if nums[i] <= nums[i+1]: ctr += 1
            else: ctr = 1
            
        for i in range(n):
            if fromleft[i] and fromright[i]: res += [i]
                
        return res
                