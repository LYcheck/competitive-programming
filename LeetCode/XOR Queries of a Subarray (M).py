class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        
        for _ in range(1, len(arr)):
            arr[_] ^= arr[_-1]
        
        for query in queries:
            if query[0] == 0:
                res.append(arr[query[1]])
            else:
                res.append(arr[query[1]] ^ arr[query[0]-1])
        
        return res