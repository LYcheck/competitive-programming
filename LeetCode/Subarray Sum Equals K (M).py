class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == k else 0

        nums = [0] + nums
        for _ in range(1, len(nums)): nums[_] += nums[_-1]
            
        print(nums)
        
        seen = {}
        res = 0
        
        for num in nums:
            if num-k in seen:
                res += seen[num-k]
                
            if num not in seen: seen[num] = 1
            else: seen[num] += 1
                
        
        print(seen)
        return res