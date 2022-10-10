class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        t = []
        for i in range(len(names)):
            t += [(heights[i], names[i])]
            
        print(t)
        res = []
        t.sort(reverse=True)
        
        for j in t:
            res += [j[1]]
            
        return res