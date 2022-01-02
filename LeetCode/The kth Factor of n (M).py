class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ctr = 0
        
        for i in range(1, n+1):
            if n % i == 0:
                ctr += 1
                
            if ctr == k:
                return i
            
        return -1
    
        #how is this a medium? I guess you can optimize to O(sqrtn) but that would have a space complexity tradeoff