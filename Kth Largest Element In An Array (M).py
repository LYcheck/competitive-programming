class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        # lol initial sol
        
        def partition(nums, l, r, k):
            pivIndex = random.randint(l, r)
            nums[pivIndex], nums[r] = nums[r],  nums[pivIndex]
            pivIndex = r
            pivot = nums[pivIndex]
            i = l
            
            for j in range(i, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    
            nums[i], nums[pivIndex] = nums[pivIndex], nums[i]
            pivIndex = i
            
            if k-1 == pivIndex:
                return nums[pivIndex]
            
            elif k-1 < pivIndex:
                return partition(nums, l, pivIndex-1, k)
            
            else:
                return partition(nums, pivIndex+1, r, k)
            
        return partition(nums, 0, len(nums) - 1, len(nums) - k + 1)
        
        n = len(nums)
        qs(nums, 0, n-1)
        
        return nums[-k]
    
    # qs implementation via ryancodrai
