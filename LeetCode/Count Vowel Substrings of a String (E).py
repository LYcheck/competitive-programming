class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if len(word) < 5:
            return 0
        
        cnt = 0
        for i in range(len(word)):
            seen = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
            res = 0
            
            for j in range(i, len(word)):
                if word[j] not in seen:
                    break
                else:
                    seen[word[j]] =1
                    
                res = all(seen[x] > 0 for x in seen.keys())
                if res:
                    cnt += 1
            
        return cnt