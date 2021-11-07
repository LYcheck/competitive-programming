class Solution:
    def countVowels(self, word: str) -> int:
        seen = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}    
        
        res = 0
        for i in range(len(word)):
            if word[i] in seen:
                res += ((len(word)-i)*(i+1))
  
        return res