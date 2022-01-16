class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        seen = {}
        for string in strings:
            tempstr = str(string)
            temp = []
            while len(tempstr) > 1:
                temp += [(ord(tempstr[1]) - ord(tempstr[0])) % 26]
                tempstr = tempstr[1:]
            ttuple = tuple(temp)
            
            if ttuple in seen: seen[ttuple] += [string]
            else: seen[ttuple] = [string]
        
        return seen.values()