class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = 0
        
        data = [0] + data
        for i in range(1, len(data)):
            if data[i]: ones += 1
            data[i] += data[i-1]
            
        res = float('inf')
        for i in range(ones, len(data)):
            seg = data[i]-data[i-ones]
            res = min(res, ones-seg)
            
        return res