from sortedcontainers import SortedList
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = SortedList()
        have = {}
        for _ in arr:
            if _ in have: continue
            else: 
                have[_] = 1
                temp.add(_)
                
        for i in range(len(temp)):
            have[temp[i]] = i+1
            
        for i in range(len(arr)):
            arr[i] = have[arr[i]]
        return arr