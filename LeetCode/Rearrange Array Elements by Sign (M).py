class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posArr = []
        negArr = []
        res = []
        
        for num in nums:
            if num < 0: negArr += [num]
            else: posArr += [num]
        
        for i in range(len(posArr)):
            res += [posArr[i]]
            res += [negArr[i]]
        
        
        return res