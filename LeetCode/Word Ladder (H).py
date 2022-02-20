class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        parents = {}
        children = {}
        
        def encode(word, parents, children):
            for i in range(len(word)):
                temp = word[:i] + '*' + word[i+1:]
                if temp in parents: parents[temp] += [word]
                else: parents[temp] = [word]
                
                if word in children: children[word] += [temp]
                else: children[word] = [temp]
        
        for word in wordList: encode(word, parents, children)
        encode(beginWord, parents, children)
        
        q = [(beginWord,1)]
        seen = {beginWord:1}
        
        while q:
            curr, dist = q.pop(0)
            if curr == endWord:
                return dist
            
            for child in children[curr]:
                for parent in parents[child]:
                    if parent not in seen: q += [(parent, dist+1)]
            
            seen[curr] = 1
        
        return 0