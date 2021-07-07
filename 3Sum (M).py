class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        
        res = list()
        nums.sort()
        
        for x in range(length):
            if x != 0 and nums[x] == nums[x - 1]:
                continue;
                
            i = x + 1
            j = length - 1
            
            while i < j:
                if nums[x] + nums[i] + nums[j] == 0:
                    res.append([nums[x], nums[i], nums[j]])
                    i += 1
                    
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                        
                elif nums[x] + nums[i] + nums[j] < 0:
                    i += 1
                    
                else:
                    j -= 1

        return res
