class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore voting algo
        
        cnt, ele = 0, nums[0]
        
        for _ in nums:
            if _ == ele:
                cnt += 1
            elif cnt == 0:
                ele = _
                cnt += 1
            else:
                cnt -= 1
        return ele