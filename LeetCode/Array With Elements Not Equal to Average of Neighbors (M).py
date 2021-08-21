class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for _ in range(1, len(nums)-1):
            if (nums[_-1] < nums[_] and nums[_] < nums[_+1]) or (nums[_-1] > nums[_] and nums[_] > nums[_+1]):
                nums[_], nums[_+1] = nums[_+1], nums[_]
        
        return nums