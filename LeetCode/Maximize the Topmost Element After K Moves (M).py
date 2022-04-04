class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0: return nums[0]
        if n == 1: return -1 if k&1 else nums[0]
        #good
        
        frownie_face = -1
        
        for i in range(min(n, k-1)):
            frownie_face = max(frownie_face, nums[i])

        if n > k:
            frownie_face = max(frownie_face, nums[k])

        return frownie_face 