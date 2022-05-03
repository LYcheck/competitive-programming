class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        have = { word:1 for word in words }
        
        def dfs(word):
            for i in range(1, len(word)):
                pre = word[i:]
                suf = word[:i]
                
                if pre in have and suf in have or pre in have and dfs(suf): return True
            return False
        
        res = []
        for word in words:
            if dfs(word): res += [word]
                
        return res