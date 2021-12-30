class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, 0
        
        # row binsearch
        u, d, m = 0, len(matrix)-1, 0
        
        while u <= d:
            m = (u+d)//2

            if matrix[m][0] == target:
                return True
            elif target >= matrix[m][0]:
                row = m
                u = m+1
            else:
                d = m-1
     
        # col binsearch
        
        l, r = 0, len(matrix[0])
        
        while l < r:
            m = (l+r)//2
            
            if matrix[row][m] == target:
                return True

            elif target > matrix[row][m]:
                l = m+1
            else:
                r = m
            
        return False