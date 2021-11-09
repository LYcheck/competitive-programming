class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        while len(a) < len(b):
            a = '0' + a
        while len(b) < len(a):
            b = '0' + b
        
        n = len(a)
        
        res = ''
        carry = 0
        for i in range(n-1, -1, -1):
            if a[i] == '1' and b[i] == '1':
                if carry:
                    res = '1' + res
                    carry = 1
                else:
                    res = '0' + res
                    carry = 1
            elif a[i] == '1' or b[i] == '1':
                if carry:
                    res = '0' + res
                    carry = 1
                else:
                    res = '1' + res
                    carry = 0

            else:
                if carry:
                    res = '1' + res
                else:
                    res = '0' + res
                
                carry = 0
            
        if carry:
            return '1'+res
        return res