class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        curVol = -1
        
        
        while right > left:
            tempVol = min(height[left], height[right]) * (right-left)
        
            if tempVol > curVol:
                curVol = tempVol
                
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return curVol
        
