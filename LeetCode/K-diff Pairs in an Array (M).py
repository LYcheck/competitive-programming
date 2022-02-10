class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = {}
        seenpairs = {}
        n = len(nums)
        nums.sort()
        
        for _ in nums:
            if _-k in seen:
                if (_, _-k) not in seenpairs:
                    seenpairs[(_, _-k)] = 1
            seen[_] = 1
            
        return len(seenpairs.keys())
                