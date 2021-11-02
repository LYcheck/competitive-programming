class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        
        for _ in range(len(nums)):
            if nums[_] in seen:
                if _-seen[nums[_]] <= k:
                    return True
            
            seen[nums[_]] = _
                
        return False