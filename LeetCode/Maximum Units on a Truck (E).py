class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        
        boxes = 0
        have = 0
        ptr = 0
        while boxes < truckSize and ptr < len(boxTypes):
            if boxTypes[ptr][0] == 0: ptr += 1
            else:
                boxTypes[ptr][0] -= 1
                boxes += 1
                have += boxTypes[ptr][1]
                
        return have