class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        idx = 0
        
        for i in range(len(arr)):
            if arr[i] not in seen:
                seen[arr[i]] = 1
            else:
                seen[arr[i]] += 1
        
        for j in range(len(arr)):
            if seen[arr[j]] == 1:
                idx += 1
            if idx == k:
                return arr[j]
                
        return ""