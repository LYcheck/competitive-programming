class Solution:
    def integerBreak(self, n: int) -> int:
        threes, twos = n//3, 0
        mod = n%3
        
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif mod == 0:
            return 3**threes
        elif mod == 1:
            threes -= 1
            return (3**threes)*2*2
        elif mod == 2:
            return (3**threes)*2
            