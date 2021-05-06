class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ch = set()
        
        for x in nums:
            if x in ch:
                return True
            else:
                ch.add(x)
        return False
