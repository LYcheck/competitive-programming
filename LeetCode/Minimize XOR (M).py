class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def cnt(n):
            tmp = 0
            while n: 
                tmp += n&1
                n>>=1
            return tmp
        
        k = cnt(num2)
        temp = 0
        
        for i in range(31, -1, -1):
            if not k: return temp
            if (num1 >> i) & 1:
                temp ^= (1 << i)
                k-=1
                
        for i in range(32):
            if not k: return temp
            if not (num1 >> i) & 1:
                temp ^= (1 << i)
                k-= 1
                
        return temp
            
                