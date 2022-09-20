class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n, res = len(arr), 0
        
        for bm in range(1 << n): # iterate thru all masks
            have, flag = set(), 1
            cursize = 0
            
            for i in range(n):
                if (bm >> i) & 1:
                    for char in arr[i]:
                        if char not in have:
                            have.add(char)
                            cursize += 1
                        else:
                            flag = 0
                            break
            if flag: res = max(res, cursize)
        return res