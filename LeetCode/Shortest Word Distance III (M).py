class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        last1, last2 = -1, -1
        flag = word1 == word2
        cand = float('inf')
                       
        for i, word in enumerate(wordsDict):
            if word == word1:
                last1 = i
                    
                if last2 != -1:
                    cand = min(cand, abs(i-last2))
                              
            if word == word2:
                last2 = i
                if not flag and last1 != -1:
                    cand = min(cand, abs(i-last1))
                
        return cand