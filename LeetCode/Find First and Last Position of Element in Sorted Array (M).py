class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(nums, x):
            l, r = 0, len(nums)-1
            
            res = [-1, -1]
            
            #left
            while (l < r):
                mid = (l + r) // 2
                
                if nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid
                    
                    
            if nums[l] != x:
                return res
            else: 
                res[0] = l

                
            #right
            r = len(nums)-1;
            while (l < r):
                mid = (l + r) // 2 + 1;
                
                if nums[mid] > x:
                    r = mid - 1
                else:
                    l = mid
                    
            res[1] = r
            
            return res
        
        if not nums:
            return [-1, -1]
        else:   
            return binSearch(nums, target)
