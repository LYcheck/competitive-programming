class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while left < right:
            
            if s[left] == s[right]:
                pass
            else:
                one = s[left:right]
                two = s[left+1:right+1]
                onecheck, twocheck = True, True
                left, right = 0, len(one)-1
                
                while left < right:
                    onecheck = onecheck and one[left] == one[right]
                    twocheck = twocheck and two[left] == two[right]
                    
                    left += 1
                    right -= 1
                        
                return onecheck or twocheck
            
            left +=1
            right -= 1
        
        return True
