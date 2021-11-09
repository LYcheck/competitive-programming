class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        
        numsa = nums[1:]
        numsb = nums[:len(nums)-1]
        
        def helprob(arr):
            twob, oneb = arr[0], max(arr[0], arr[1])
            curr = 0
            
            for i in range(2, len(arr)):
                curr = max(arr[i] + twob, oneb)
                twob = oneb
                oneb = curr
            
            return curr
        
        return max(helprob(numsa), helprob(numsb))