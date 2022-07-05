class Solution:
    def topKFrequent(self, words: List[str], p: int) -> List[str]:
        def comparator(t1, t2):
            freq1, word1 = t1
            freq2, word2 = t2
            
            if freq1 < freq2: return 1
            elif freq2 < freq1: return -1
            else:
                if word1 == word2: return 0
                return 1 if word1 > word2 else -1
        
        res = []
        freq = {}
        for word in words:
            if word in freq: freq[word] += 1
            else: freq[word] = 1
                
        k = list(freq.keys())
        
        for key in k: res += [(freq[key], key)]
        res.sort(key=cmp_to_key(comparator))
        
        return [ res[i][1] for i in range(p)]