class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if not nums[0]: nums[0] = -1
        seen = {nums[0]:0}
        best = 0
        for i in range(1,len(nums)):
            if not nums[i]: nums[i] = -1
            nums[i] += nums[i-1]
            if nums[i] not in seen:
                seen[nums[i]] = i
            
            if not nums[i]: best = i+1
            elif nums[i] in seen:
                best = max(best, i-seen[nums[i]])
        
        return best