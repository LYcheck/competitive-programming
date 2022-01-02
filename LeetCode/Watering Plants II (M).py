class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ctr = 0
        acap, bcap = capacityA, capacityB
        n = len(plants)
        
        l, r = 0, n-1
        while l < r:
            if acap < plants[l]:
                acap = capacityA
                ctr += 1
            
            acap -= plants[l]
            l+=1
            
            if bcap < plants[r]:
                bcap = capacityB
                ctr += 1
                
            bcap -= plants[r]
            r -= 1
            
            if l == r:
                if acap >= plants[l] or bcap >= plants[r]:
                    return ctr
                else:
                    return ctr+1
                
        return ctr
            