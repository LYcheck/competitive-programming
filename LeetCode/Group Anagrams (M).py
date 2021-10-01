class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = list()
        seen = dict()
        
        for word in strs:
            s = str(word)
            s = "".join(sorted(s))
            
            if s in seen:
                seen[s].append(word)
            else:
                seen[s] = [word]
            
        for word in seen.keys():
            res.append(seen[word])
            
        return res