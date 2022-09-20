class Solution:
    def isStrictlyPalindromic(self, num: int) -> bool:
        def base(n, b):
            if n == 0: return [0]
            digits = []
            while n:
                digits.append(str(n % b))
                n //= b
            return ''.join(digits[::-1])
        
        for i in range(2, num-1):
            temp = base(num, i)
            if temp != temp[::-1]: return False
            
        return True
        