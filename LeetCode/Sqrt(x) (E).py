class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if x >= mid*mid:
                left = mid+1
                ans = mid
            else:
                right = mid - 1
        
        return ans
