class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        triangle.append([0]*(len(triangle[-1])+1))
        
        if n == 1:
            return triangle[0][0]
        
        for i in range(n-1, -1, -1):
            if i == 0:
                return triangle[0][0] + min(triangle[1][0], triangle[1][1])
            else:
                for j in range(i+1):
                    triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])