class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tort, hare = nums[0], nums[0]
        
        while 1:
            tort = nums[tort]
            hare = nums[nums[hare]]
            
            if hare == tort:
                break
            
        tort = nums[0]
        
        while hare != tort:
            tort = nums[tort]
            hare = nums[hare]
        
        return hare