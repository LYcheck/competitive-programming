class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        test = 0
        
        for _ in nums:
            test ^= _
        
        testbit = (~test + 1) & test
        test2 = 0
        
        for _ in nums:
            if _ & testbit == testbit:
                test2 ^= _
            
        return [test2, test^test2]
