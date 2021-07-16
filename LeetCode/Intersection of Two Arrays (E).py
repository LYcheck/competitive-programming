class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #ans = set()
        #for x in nums1:
        #    if x in nums2:
        #        ans.add(x)
        
        return set(nums1) & set(nums2)
