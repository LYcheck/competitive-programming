class Solution:
    def maximum69Number (self, num: int) -> int:
        ints = list(str(num))
        
        for i in range(len(ints)):
            if ints[i] == '6':
                ints[i] = '9'
                break
        
        return int(''.join(map(str, ints)))