class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n, idx, prod, pow = len(s), 0, 0, 1
        
        for _ in range(k):
            prod += (ord(s[_])-ord('a')+1)*pow
            if _ != k-1: pow *= power
        
        while idx < n:
            if prod%modulo == hashValue:
                return s[idx:idx+k]
            else:
                prod -= ord(s[idx])-ord('a')+1
                prod //= power
                prod += (ord(s[idx+k])-ord('a')+1)*pow
                idx += 1