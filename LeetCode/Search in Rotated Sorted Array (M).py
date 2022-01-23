class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        while l < r:
            m = (l+r)//2 
            
            if nums[m] > nums[r]: l = m+1
            else: r = m
        
        piv = l
        l, r = 0, n-1
        
        while l<=r:
            m = (l+r) // 2
            pivm = (m+piv)%n
                
            if nums[pivm] == target: return pivm
            elif nums[pivm] > target: r = m-1
            else: l = m+1
            
        return -1