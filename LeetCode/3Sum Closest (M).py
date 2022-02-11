class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = -float('inf')
        
        for i in range(n):
            n1 = nums[i]
            targ = target - n1
            i2, i3 = i+1, n-1
            
            while i2 < i3:
                n2 = nums[i2]
                n3 = nums[i3]
                
                diff = targ-n2-n3
                if abs(target-best) > abs(diff): best = n1+n2+n3
                
                if n2+n3 > targ:
                    i3-=1
                else:
                    i2+=1
                    
        return best