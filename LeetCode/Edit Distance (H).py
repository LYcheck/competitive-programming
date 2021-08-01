class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Levenshtein Distance algo - not reinventing the wheel

        arr = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        
        for i in range(len(word1)+1):
            arr[i][0] = i
            
        for j in range(len(word2)+1):
            arr[0][j] = j
            
        for k in range(1, len(word1)+1):
            for a in range(1, len(word2)+1):
                if word1[k-1] == word2[a-1]:
                    arr[k][a] = arr[k-1][a-1]
                else:
                    ins = 1+arr[k][a-1]
                    de = 1+arr[k-1][a]
                    rep = 1+arr[k-1][a-1]
                    
                    arr[k][a] = min(ins, de, rep)
        
        return arr[len(word1)][len(word2)]