class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.cache = dict()
        
        for i in range(len(wordsDict)):
            word = wordsDict[i]
            if word in self.cache:
                self.cache[word].append(i)
            else:
                self.cache[word] = [i]
        

    def shortest(self, word1: str, word2: str) -> int:
        best = float('inf')
        w1 = self.cache[word1]
        w2 = self.cache[word2]
        
        i = 0
        j = 0
        
        while i < len(w1) and j < len(w2):
            best = min(best, abs(w1[i]-w2[j]))
                
            if w1[i] < w2[j]:
                i += 1
            else:
                j += 1
        
        return best


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)