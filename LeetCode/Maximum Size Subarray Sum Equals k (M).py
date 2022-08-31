class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = {0: 0}
        nums = [0] + nums
        res = 0
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i] not in seen: seen[nums[i]] = i
                
            # k = nums[i] - x
            # x = nums[i] - k
            if (nums[i] - k) in seen: res = max(res, i-seen[(nums[i]-k)])
                
        return res