class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for x in range(len(digits)-1, -1, -1): # <--
            if digits[x] != 9:
                digits[x] += 1
                return digits
            elif digits[x] == 9 and x == 0:
                digits[x] = 0
                digits.insert(0,1)
                return digits
            else:
                digits[x] = 0
        
        return digits
