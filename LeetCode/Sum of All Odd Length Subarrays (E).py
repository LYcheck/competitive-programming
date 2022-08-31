class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
            
        res = 0
        
        for i in range(len(arr)):
            temp = 0
            for j in range(0, i, 2):
                if j == 0: temp += arr[i]
                else: temp += arr[i] - arr[j-1]
                    
        return res
                