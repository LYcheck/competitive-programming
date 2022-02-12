class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0]*(length+1)
        
        for update in updates:
            nums[update[0]+1] += update[2]
            
            if update[1]+2 < length+1: nums[update[1]+2] -= update[2]
            
        for _ in range(1, length+1):
            nums[_] += nums[_-1]
        
        return nums[1:]