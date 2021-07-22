class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        letters = list(brokenLetters)
        ans = len(words)
        
        for _ in words:
            for i in _:
                if i in letters:
                    ans -= 1
                    break
                    
        return ans
