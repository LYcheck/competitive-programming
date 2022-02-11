class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        seen = {}
        
        for i in range(n):
            for j in range(i+1, n):
                n1, n2 = nums[i], nums[j]
                l = j+1
                r = n-1
                targ = target-n1-n2
                while l < r:
                    n3 = nums[l]
                    n4 = nums[r]
                    
                    if n3+n4 > targ:
                        r -= 1
                    elif n3+n4 < targ:
                        l += 1
                    else:
                        temp = tuple([n1, n2, n3, n4])
                        if temp not in seen:
                            res += [[n1, n2, n3, n4]]
                            seen[temp] = 1
                        l += 1
            
        return res