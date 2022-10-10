class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums2)&1:
            for _ in nums1: res ^= _
        if len(nums1)&1:
            for _ in nums2: res ^= _
                
        return res